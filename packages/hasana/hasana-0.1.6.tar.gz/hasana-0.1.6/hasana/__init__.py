from __future__ import print_function
import os, sys, pwd, json, asana, datetime,time,string,pytz,base64
from datetime import date, timedelta
from datetime import datetime as sub
from dateutil.parser import *
from zlib import compress
from six import print_
import funbelts as ut

import six
if six.PY2:
	from string import maketrans
else:
	maketrans = bytes.maketrans

est =  pytz.timezone('US/Eastern')

##Stub of encapsulating a diagram to pass to kroki
##Kroki Live Editor isn't capable of large form gantt charts
def kroki_wrap(content):
    import sys, base64, zlib
    return base64.urlsafe_b64encode(zlib.compress(content.encode('utf-8'), 9)).decode('ascii')

def kroki_gantt(content):
    return "https://kroki.io/mermaid/svg/{0}".format(kroki_wrap(content))

def plant(plantuml_text, _type='svg'):
		base = f'''https://www.plantuml.com/plantuml/{_type}/'''

		plantuml_alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase + '-_'
		base64_alphabet   = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
		b64_to_plantuml = maketrans(base64_alphabet.encode('utf-8'), plantuml_alphabet.encode('utf-8'))

		"""zlib compress the plantuml text and encode it for the plantuml server.
		"""
		zlibbed_str = compress(plantuml_text.encode('utf-8'))
		compressed_string = zlibbed_str[2:-4]
		return base+base64.b64encode(compressed_string).translate(b64_to_plantuml).decode('utf-8')

def plant_gantt(content):
    return plant(content + "\n@endgantt")

#https://developers.asana.com/docs/create-a-task
#Custom Fields/Opt_Fields   

class masana(object):
    def __init__(self,access_token:str=None,workspace_choice:str="Personal", project_choice:str=None):
        self.client = asana.Client.access_token(access_token)

        self.current_project = None
        self.project = None

        self.current_workspace = None
        self.workspace = None

        self.current_user = self.client.users.me()
        self.user = self.current_user['gid']
        
        self.added_tasks = {}
        self._tags = []
        self._projects = []
        self._tasks = []
        self._full_tasks = []
        self._detailed_tasks = []
        
        #https://developers.asana.com/docs/custom-fields
        #self._priority = []
        if project_choice and workspace_choice:
            self.current_workspace = [x for x in list(self.client.workspaces.find_all()) if x['name'] == workspace_choice][0]
            self.workspace = self.current_workspace['gid']
            
            self.current_project = [x for x in list(self.client.projects.find_all({
                'workspace':self.workspace
            })) if x['name'] == project_choice][0]
            self.project = self.current_project['gid']
        elif workspace_choice:
            self.current_workspace = [x for x in list(self.client.workspaces.find_all()) if x['name'] == workspace_choice][0]
            self.workspace = self.current_workspace['gid']
    def complete_old_tasks(self, up_to_date:sub.now()):
        for task in self.full_tasks(['assignee', 'due_on']):
            if task['gid'] == self.user and sub.strptime(task['due_on'], '%Y-%m-%d') < up_to_date:
                self.complete_task(task['gid'])
    def pick_workspace(self, choice:int):
        self.current_workspace = list(self.client.workspaces.find_all())[choice]
        self.workspace = self.current_workspace['gid']
        return self.current_workspace
    def default_workspace(self):
        return self.pick_workspace(0)
    @property
    def old_priorities(self):
        #if self._priority == []:
            #https://developers.asana.com/docs/get-a-workspaces-custom-fields
            #self._priority = [x for x in list(self.client.custom_fields.get_custom_fields_for_workspace(self.workspace)) if x['name'] == 'Priority']['enum_options']
        return self._priority
    @property
    def tags(self):
        if self._tags == []:
            self._tags = list(self.client.tags.get_tags_for_workspace(self.workspace))
        return self._tags
    def add_tag(self, string_name):
        tag = self.client.tags.create_tag({
            'name':string_name,
            'workspace':self.workspace
        })
        self._tags += [tag]
        return tag
    @property
    def projects(self):
        if self._projects == []:
            self._projects = list(self.client.projects.get_projects({'workspace':self.workspace},opt_fields=['name']))
        return self._projects
    def section_per_project(self, project_gid, name:str=None):
        #https://developers.asana.com/reference/getsectionsforproject
        tasks = list(self.client.sections.get_sections_for_project(project_gid,opt_fields=['name']))
        if name:
            for task in tasks:
                if task["name"] == name:
                    return task
            return None
        else:
            return tasks
    def add_project(self, project:str):
        #https://developers.asana.com/docs/create-a-project
        result = self.client.projects.create_project({
            'name':project,
            'public':False,
            'owner':self.user,
            'default_view':'list',
            'workspace':self.workspace
        })
        self._projects += [result]
        return result
    def get_tasks_from_project(self, project_gid, log:bool=False):
        output = []
        if project_gid:
            output = self.client.tasks.get_tasks_for_project(project_gid)
        elif log:
            print("Project gid is empty")
        return output
    def get_project(self,project:str):
        #https://developers.asana.com/docs/get-multiple-projects
        if project is not None and self.current_workspace != None:
            found = None
            #https://book.pythontips.com/en/latest/for_-_else.html
            for proj in self.projects:
                if proj['name'] == project:
                    found = proj
                    break
            else:
                found = self.add_project(project)
            return found
        return None
    def del_project(self,project:str=None,project_gid=None, log:bool=False):
        """
        https://developers.asana.com/docs/delete-a-project
        """
        current_project = self.get_project(project)
        if current_project and not project_gid:
            project_gid = current_project['gid']

        if project_gid is not None:
            self.client.projects.delete_project(project_gid)
            return True
        else:
            if log:
                print("No Project information is passed")
            return False
    def pick_project_string(self,choice:str):
        #https://developers.asana.com/docs/get-multiple-projects
        if self.current_workspace != None:
            project = None
            for proj in self.client.projects.get_projects({
                'workspace': self.workspace
            }):
                if proj['name'] == choice:
                    project = proj
            if project is not None:
                self.current_project = project
                self.project = project['gid']
        return self.current_project
    def pick_project(self,choice:int):
        if self.current_workspace != None:
            self.current_project = list(self.client.projects.find_all({
                'workspace':self.workspace
            }))[choice]
            self.project = self.current_project['gid']
        return self.current_project
    def default_project(self):
        return self.pick_project(0)
    def defaults(self):
        self.default_workspace()
        self.default_project()
    def delete(self, task_id):
        self.client.tasks.delete_task(task_id)
    def refresh_tasks(self):
        self.tasks(True)
    @property
    def mytasks(self):
        return self.tasks(False)
    def tasks(self, refresh:bool):
        if self.current_workspace == None or self.current_project == None:
            self._tasks = []
        elif self._tasks == [] or refresh:
            self._tasks = list(self.client.tasks.get_tasks_for_project(self.project))
        return self._tasks
    def full_tasks(self, fields=[], log=False):
        try:
            return list(self.client.tasks.get_tasks({
                'assignee': self.user,
                'workspace':self.workspace,
                'opt_fields':fields
            }))
        except Exception as e:
            if log:
                print(e)
            return []
    @property
    def clearcache(self):
        self._detailed_tasks = []
    @property
    def taskz(self):
        if self._detailed_tasks is None or self._detailed_tasks == []:
            self._detailed_tasks = [self.get_task_detail(x['gid']) for x in self.full_tasks()]
        return self._detailed_tasks
    def tasks_by_date(self, date:datetime.datetime, completed=False,fields=[],log=False):
        """
        https://developers.asana.com/docs/search-tasks-in-a-workspace

        https://stackoverflow.com/questions/2150739/iso-time-iso-8601-in-python
        https://stackoverflow.com/questions/4460698/python-convert-string-representation-of-date-to-iso-8601
        """
        output = []
        try:
            if log:
                print("Looking for dasks due by " + date.isoformat())
            
            if False: #SEARCH IS PREMIUM ONLY
                output = list(self.client.tasks.search_tasks_for_workspace(self.workspace, {
                    'due_by': str(date.isoformat())
                }))
            else:
                #https://developers.asana.com/docs/get-multiple-tasks
                """
                Mass getting and manually filtering
                """
                flag = False
                if log:
                    print('[',end='',flush=True)
                for itr, task in enumerate(self.full_tasks(fields=['due_at','due_on','completed']+fields,log=log)):
                    date = date.astimezone(est)

                    if task['due_on'] is not None:
                        #due_on = sub.strptime(task['due_on'], '%Y-%m-%d')
                        due_on = parse(task['due_on']).astimezone(est) #.strptime(task['due_on'], '%Y-%m-%d')
                    else:
                        due_on = None
                    if task['due_at'] is not None:
                        due_at = parse(task['due_at']).astimezone(est) #, 'Y-%m-%dT%H:%M:%S.%fZ')##'%Y-%m-%dT%H:%M:%S.000')
                        #due_at = sub.fromisoformat(task['due_at'])#strptime(task['due_at'], '%Y-%m-%dT%H:%M:%S.000')
                    else:
                        due_at = None
                    """
                    datetime. strptime(date_time_str, '%d/%m/%y %H:%M:%S')
                    
                    if (
                            (due_at is not None and date.replace(hour=0,minute=0) < due_at < date)
                            or 
                            (due_on is not None and date.replace(hour=0,minute=0,second=0) <= due_on <= date)
                        ):
                        if not flag:
                            flag = True
                        if completed is None or completed == task['completed']:
                            output += [task]
                    """
                    if log:
                        print('.',end='',flush=True)
                if log:
                    print(']',flush=True)
        except Exception as e:
            if log:
                print(e)
            pass
        return output
    def get_project_detail(self, proj_id):
        # Create a Project :> https://developers.asana.com/reference/createproject
        #https://github.com/Asana/python-asana/blob/master/asana/resources/projects.py#L55
        try:
            return self.client.projects.get_project(proj_id, opt_fields = [
                "name",
                "string",
                "color",
                "current_status",
                "current_status_update",
                "default_view",
                "due_date",
                "due_on",
                "html_notes",
                "is_template",
                "notes",
                "public",
                "start_on",
                "custom_fields",
                "followers",
                "owner",
                "team",
            ])
        except Exception as e:
            print(e)
        return []
    def get_task_detail(self, task_id):
        #https://developers.asana.com/docs/create-a-task
        task = self.client.tasks.get_task(task_id,opt_fields = [
            'name',
            'owner',
            'description',
            'notes',
            'projects',
            'workspace',
            'resource_subtype',
            'html_notes',
            'resource_subtype',
            'assignee_status',
            'assignee_section',
            'completed',
            'created_at',
            'created_on',
            'due_at',
            'due_on',
        ])

        task['project_details']={}
        for project in task['projects']:
            project_sections = self.section_per_project(project['gid'])

            cur = self.get_project_detail(project['gid'])
            task['project_details'][project['gid']] = cur
            
            if "assignee_section" in cur and cur["assignee_section"] != {}:
                for project_section in project_sections:
                    if cur["assignee_section"]["gid"] == project_section["gid"]:
                        task['project_details'][project['gid']]["assignee_section"] = project_section["name"]
                        break

            if "assignee_section" not in task['project_details'][project['gid']] or not isinstance(task['project_details'][project['gid']]["assignee_section"], str):
                task['project_details'][project['gid']]["assignee_section"] = ""
        
        return task
    def tasks_in_x_days(self, xdays=0, fields=[],log=False):
        output = []
        now = datetime.datetime.now(pytz.timezone('US/Eastern'))
        now = now + datetime.timedelta(days=xdays)
        taskz = self.full_tasks(fields=['due_at','due_on','completed','name','description'],log=log)

        for itr, task in enumerate(taskz):
            if not task['completed']:
                due_on, due_at, workingdate = None, None, None
                try:
                    due_on = datetime.datetime.strptime(task['due_on'], '%Y-%m-%d')
                except: pass
                try:
                    due_at = datetime.datetime.strptime(
                        str(task['due_on']).replace('Z',''),
                        '%Y-%m-%dT%H:%M:%S.%f'
                    ) #'2023-04-11T09:00:00.000Z'
                except: pass

                if due_on is not None:
                    workingdate = due_on
                elif due_at is not None:
                    workingdate = due_at
                else:
                    break
        
                if now.day == workingdate.day and now.month == workingdate.month and now.year == workingdate.year:
                    output += [task]

        return output

    def tasks_by_tonight(self, fields=[],log=False):
        return self.tasks_in_x_days(fields=fields,log=log)
    def task_by_id(self, id):
        return self.client.tasks.get_task(id)
    def complete_task(self,id,log=False):
        #https://developers.asana.com/docs/update-a-task
        output = False
        try:
            self.client.tasks.update_task(id,{
                'completed':True
            })
        except Exception as e:
            if log:
                print(e)
            pass
        return output
    def add_project_to_task(self, task_gid:int, project_strings=None):
        if task_gid is None or project_strings is None:
            return False
        for string in project_strings:
            if project := self.get_project(string):
                try:
                    """
                    https://developers.asana.com/docs/add-a-project-to-a-task
                    """
                    self.client.tasks.add_project_for_task(task_gid, {
                        'project':project['gid']
                    })
                except Exception as e:
                    print('Issue '+str(e))
                    pass
        return True
    def get_tasks_per_project(self,project:str):
        try:
            cur_proj = self.pick_project_string(project)
            output = list(self.client.tasks.get_tasks_for_project(cur_proj['gid']))
            return output
        except Exception as e:
            print(":> "+str(e))
            return []    
    def gantturl_per_project(self,project:str,string_date_lambda=None, task_specify_lambda=None):
        content = """@startgantt
title Overall Gantt Chart
dateFormat YYY-MM-DD"""
        content = """@startgantt
printscale daily zoom 2
"""
        if project is None:
            projects = self.projects
        else:
            projects = [project]
        
        for tproj in projects:
            content += self.gantt_per_project(tproj,string_date_lambda, task_specify_lambda)
        
        return plant_gantt(content) #kroki_gantt(content)
    def gantt_per_project(self,project:str,string_date_lambda=None, task_specify_lambda=None):
        tasks = self.get_tasks_per_project(project)
        start_date = ""
        content = """
section Project {0} Work
""".format(project.title().replace('-',''))
        content = """
-- {0} --
Project starts <X>
<TODAY> is colored in salmon
""".format(project.title().replace('-',''))
        list_of_dates = []
        for task_itr,task in enumerate(tasks):
            task_detail = self.get_task_detail(task['gid'])
            if task_specify_lambda is None or task_specify_lambda(task_detail):
                created_on = sub.strptime(str(task_detail['created_at']).split('.')[0],'%Y-%m-%dT%H:%M:%S').strftime("%Y-%m-%d")
                
                #if task_itr == 0:
                #    content = content.replace('Project starts <X>','Project starts {0}'.format(created_on))

                if False:
                    content += "{0}  :task{1}, {2} {3}, {4}\n".format(
                        task['name'],task_itr,'done,' if task_detail['completed'] else '', created_on, task_detail['due_on']
                    )
                else:
                    if task_detail['due_on'] and task_detail['due_on'].strip() != '' and (string_date_lambda is None or string_date_lambda(task_detail['due_on'])):

                        #og_content = "[{0}] starts {1}".format(task['name'],created_on) + "\n" + "[{0}] ends {1}".format(task['name'],task_detail['due_on']) + "\n"
                        #backcontent = "[{0}] ends {1}".format(task['name'],task_detail['due_on']) + "\n"

                        for line in task_detail['notes'].split('\n'):
                            if line.startswith("START="):
                                created_on = line.replace("START=","")

                        list_of_dates += [
                            sub.strptime(created_on, "%Y-%m-%d")
                        ]

                        if task['resource_subtype'].strip() == 'milestone':
                            content += "[{0}] happens {1}".format(task['name'],task_detail['due_on']) + "\n"
                        else:
                            content += "[{0}] starts {1}".format(task['name'],created_on) + "\n" + "[{0}] ends {1}".format(task['name'],task_detail['due_on']) + "\n"

                        if task_detail['completed']:
                            content += "[{0}] is 100%% complete".format(task['name']) + "\n"

        if len(list_of_dates) == 0:
            list_of_dates += [datetime.datetime.now()]

        content = content.replace('Project starts <X>','Project starts {0}'.format(min(list_of_dates).strftime("%Y-%m-%d")))
        content = content.replace(
            "<TODAY> is colored in salmon",
            "{0} is colored in salmon".format(
                datetime.datetime.now().strftime("%Y-%m-%d")
            )
        )
                

        return str(content) + "\n"
    def get_tasks(self, project:str=None, waiting:int=1):
        if self.current_workspace == None:
            return []
        elif self._full_tasks != []:
            return self._full_tasks

        #https://developers.asana.com/docs/get-multiple-tasks
        if project == None:
            tasks = list(self.client.tasks.get_tasks({
                'workspace':self.workspace,
                'assignee':self.user
            }))
        else:
            tasks = list(self.client.tasks.get_tasks_for_project(self.project))

        #https://developers.asana.com/docs/get-a-task
        for x in tasks:
            self._full_tasks += [self.client.tasks.get_task(x['gid'])]
            if waiting > 0:
                print(".",end='',flush=True)
                time.sleep(waiting)
        return self._full_tasks
        """
        return [
                self.client.tasks.get_task(x) for x in tasks
        ]
        """
    def add_tags_to_task(self,taskid,tags=[]):
        """
        for tag in tags:
            try:
                #https://developers.asana.com/docs/get-tags-in-a-workspace
                #Identifying Tags
                current_tags = list(self.client.tags.get_tags_for_workspace(self.workspace))
                searched_tag = [x for x in current_tags if x['name'] == tag]
                if len(searched_tag) > 0:
                    found_tag = searched_tag[0]
                else: #https://developers.asana.com/docs/create-a-tag
                    found_tag = self.client.tags.create_tag({
                        'name':tag
                    })
                #https://developers.asana.com/docs/add-a-tag-to-a-task
                self.client.tasks.add_tag_for_task(
                    taskid,
                    {
                        'tag':found_tag['gid']
                    }
                )
            except Exception as e:
                print(f"!!Exception {e}")
                pass
        """
        for tag in tags:
            try:
                searched_tag = [x for x in self.tags if x['name'] == tag]
                if len(searched_tag) > 0:
                    found_tag = searched_tag[0]
                else: #https://developers.asana.com/docs/create-a-tag
                    found_tag = self.add_tag(tag)
                self.client.tasks.add_tag_for_task(
                    taskid,
                    {
                        'tag':found_tag['gid']
                    }
                )
            except Exception as e:
                print(f"!!Exception {e}")
                pass
    def add_task(self, name:str, notes:str=None, due_day:str=None, sub_task_from:int=None, tags=[], projects=[]):
        if self.current_workspace == None or (self.current_project == None and projects == [] and sub_task_from == None):
            return None
        
        if due_day is not None:
            current_date = str(est.localize(datetime.datetime.utcnow()).isoformat()).split('T')[0]
            due_day = due_day or current_date

            if False:
                if due_time is not None:
                    #https://stackoverflow.com/questions/12691081/from-a-timezone-and-a-utc-time-get-the-difference-in-seconds-vs-local-time-at-t
                    local = datetime.datetime.now()
                    utc = datetime.datetime.utcnow()
                    diff = int((local - utc).days * 86400 + round((local - utc).seconds, -1))
                    hours = datetime.timedelta(seconds=diff)
                    hours, _ = divmod(hours.seconds, 3600)

                    due_time = f"{due_time.hour + hours}:{due_time.minute}:{due_time.second}.000"
                else:
                    due_time = "22:00:00"

            #http://strftime.net/
            try:
                due_date = f"{est.localize(due_day).strftime('%Y-%m-%dT%H:%M:%SZ')}"
            except:
                due_date = f"{due_day.strftime('%Y-%m-%dT%H:%M:%SZ')}"
        else:
            due_date = None
        
        #Examples
        #https://github.com/Asana/python-asana/tree/master/examples
        task = None

        if False:
            for tag in tags:
                #https://developers.asana.com/docs/create-a-tag
                self.client.tags.create_tag(self.workspace, tag)

        current_projects = [self.project] if self.project is not None else [self.get_project(x)['gid'] for x in projects]

        if sub_task_from is not None:
            parent_task = self.client.tasks.get_task(sub_task_from)

            #https://developers.asana.com/docs/create-a-subtask
            try:
                task_id = self.client.tasks.create_subtask_for_task(sub_task_from,{
                    'name': name,
                    'assignee':self.user,
                    'approval_status': 'pending',
                    'notes':notes,
                    'workspace':self.workspace,
                    'projects': [x['gid'] for x in parent_task['projects']],
                    'due_at':sub.strptime(parent_task['due_at'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%dT%H:%M:%SZ')
                }, opt_fields=['gid'])
                task = self.client.tasks.get_task(task_id['gid'])
                self.add_tags_to_task(task_id['gid'], tags)
            except Exception as e:
                print(f"!Exception {e}")
                pass
        else:
            task_id = None
            try:
                #https://developers.asana.com/docs/create-a-task
                #https://github.com/Asana/python-asana/blob/master/asana/resources/tasks.py#L38
                task_id = self.client.tasks.create_in_workspace(
                    self.workspace,
                    {
                       'assignee':self.user,
                       'name':     name,
                       'notes':    notes,
                       'projects': current_projects,
                       'due_at':due_date
                    },
                    opt_fields=['gid']
                )['gid']
            except Exception as e:
                print(f">Exception {e}")
                pass
            if task_id is None:
                return None

            print(f"Current Task ID {task_id}")
            task = self.client.tasks.get_task(task_id)

            #https://developers.asana.com/docs/update-a-task
            try:
                self.client.tasks.update_task(task_id,
                    {
                        'approval_status': 'pending',
                        'notes':notes,
                        'workspace':self.workspace,
                    })
            except Exception as e:
                print(f"$Exception {e}")
                pass
        
            try:
                self.add_tags_to_task(task_id, tags)
            except Exception as e:
                print(f"%>Exception {e}")
                pass
        
        self.add_project_to_task(task['gid'], projects)

        if task is not None:
            self.added_tasks[task['gid']] = task

        return task
    def add_task_nextdays(self, name:str, notes:str=None, in_x_days:int=None, due_day:datetime=None, sub_task_from:int=None, tags=[], projects=[]):
        current_day = datetime.datetime.utcnow()
        if due_day is None:
            due_day = current_day
        
        #nice_day = due_day.replace(day=current_day + datetime.timedelta(days=in_x_days))

        return self.add_task(name=name, notes=notes, due_day=nice_day,sub_task_from=sub_task_from, tags=tags, projects=projects)
    def add_reoccuring_task(self, name:str, notes:str=None, for_x_days:int=None, until:str=None, due_date:datetime=None, sub_task_from:int=None, tags=[], projects=[], hour:int=None,minute:int=0,second:int=0, waiting:int=5):
        output = []

        if due_date is None:
            sdate = datetime.datetime.utcnow()
        else:
            sdate = due_date
        
        #TimeReplace https://stackoverflow.com/questions/12468823/python-datetime-setting-fixed-hour-and-minute-after-using-strptime-to-get-day
        if hour is not None:
            local = datetime.datetime.now()
            utc = datetime.datetime.utcnow()
            diff = int((local - utc).days * 86400 + round((local - utc).seconds, -1))
            #sdate=sdate.replace(hour=hour+diff)
        """
        if minute is not None:
            sdate=sdate.replace(minute=minute)
        if second is not None:
            sdate=sdate.replace(second=second)
        """
        if for_x_days is not None:
            edate = sdate + datetime.timedelta(days=for_x_days+1)
        else:
            edate = until + datetime.timedelta(days=2)

        range_of_days = [sdate+timedelta(days=x) for x in range((edate-sdate).days)]
        for day in range_of_days:
            if True:
                output += [
                    self.add_task(name=name, notes=notes, due_day=day,sub_task_from=sub_task_from, tags=tags,projects=projects)
                ]
                print(f"Waiting for {waiting} seconds")
                time.sleep(waiting)
            else:
                print(day)
        return output
        def easy_add_reoccurring_tasks(self,name:str,notes:str=None,pandas_daterange=None, tags=[], projects=[], waiting:int=5):
            output = []
            for day in pandas_daterange:
                output += [
                    self.add_task(name=name, notes=notes, due_day=day,sub_task_from=sub_task_from, tags=tags,projects=projects)
                ]
                print(f"Waiting for {waiting} seconds")
                time.sleep(waiting)
            return output
