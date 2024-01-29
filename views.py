from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from apps.utils import dictfetchall
from apps.iotapi.models import *


class ProjectsCrud(APIView):

    def get(self,request,recno = None):

        success = False

        try:
            if recno:                       # it checks if any value passed in payload or not
                get = "SELECT * FROM projects WHERE recno = %s "   # AND active = True"
                with connection.cursor() as c:
                    c.execute(get, [recno])
                    row = dictfetchall(c)
                success = True
            else:
                get = "SELECT * FROM projects"      # WHERE active = True"
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)                       # write code for dictfetchall
                success = True

            return Response({'Success' : success, 'Message' : row}, status=200)

        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    def post(self,request):
        
        success = False
        try:
            request_data = request.data
            
            #recno = request_data['recno']
            descn = request_data['descn']

            """name = request_data['name']
            email = request_data['email']"""
            #trdate = getToday()

            # active = request_data.get('active', 1)

            #serializer = Tenantsserializer(data = request.data)

            # if serializer.is_valid():
            if descn != None:
                add = "INSERT INTO projects (descn) VALUES (%s)"

                with connection.cursor() as c:
                    c.execute(add, [descn])
                
                get = "SELECT * FROM projects ORDER BY recno DESC LIMIT 1"
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)

                success = True

                return Response({'Success': success, 'Message': row}, status=200)
            
            else:

                return Response({'Success': success, 'Error': 'try again'}, status=400)
            
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    def patch(self, request):

        success = False
        try:
            request_data = request.data
            recno = request_data.get('recno',None)
            descn = request_data.get('descn')

            """name = request_data.get('name',None)
            email = request_data.get('email',None)"""
            
            
            #active = request_data.get('active', 1)

            # try:
            #     tenants_obj = USER.objects.get(recno = recno)
            # except:
            #     raise Exception({'Success': success, 'Error': 'Not Found'})
            
            # schemes = request_data['schemes']
            # active = request_data.get('active', 1)

            # update = 'UPDATE test_table SET name = %s,email = %s, active = %s WHERE recno = %s'
            # with connection.cursor() as c:
            #     c.execute(update, [name,email,active,recno])

            update = f"UPDATE projects SET descn = '{descn}' WHERE recno = {recno}"
            with connection.cursor() as c:
                c.execute(update)
            success = True

            return Response({'Success': success, 'Message': 'Updated Successfully'}, status= 200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    """def delete(self, request):

        # success = False

        try:
            request_data = request.data
            recno = request_data['recno']

            delete = 'UPDATE test_table SET active = False WHERE recno = %s'

            with connection.cursor() as c:
                c.execute(delete, [recno])
            
            success = True
            return Response({'Success': success, 'Message': 'Deleted Successfully'}, status=200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : False, 'Error' : str(err)}, status=400)"""

class SensordataCrud(APIView):

    def get(self,request,recno = None):

        success = False

        try:
            if recno:                       # it checks if any value passed in payload or not
                get = "SELECT * FROM sensordata WHERE recno = %s "   # AND active = True"
                with connection.cursor() as c:
                    c.execute(get, [recno])
                    row = dictfetchall(c)
                success = True
            else:
                get = "SELECT * FROM sensordata"      # WHERE active = True"
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)                       # write code for dictfetchall
                success = True

            return Response({'Success' : success, 'Message' : row}, status=200)

        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    def post(self,request):
        
        success = False
        try:
            request_data = request.data
            
            #recno = request_data['recno']
            
            trdate = getToday()
            trtime = getlocaltime()
            valuedata = request_data['valuedata']

            """name = request_data['name']
            email = request_data['email']"""
            #trdate = getToday()

            # active = request_data.get('active', 1)

            #serializer = Tenantsserializer(data = request.data)

            # if serializer.is_valid():
            if valuedata != None:
                add = "INSERT INTO sensordata (trdate,trtime,valuedata) VALUES (%s, %s, %s)"

                with connection.cursor() as c:
                    c.execute(add, [trdate,trtime,valuedata])
                
                get = "SELECT * FROM sensordata ORDER BY recno DESC LIMIT 1"
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)

                success = True

                return Response({'Success': success, 'Message': row}, status=200)
            
            else:

                return Response({'Success': success, 'Error': 'try again'}, status=400)
            
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    def patch(self, request):

        success = False
        try:
            request_data = request.data
            recno = request_data.get('recno',None)
            valuedata = request_data.get('valuedata')            
            
            #active = request_data.get('active', 1)

            # try:
            #     tenants_obj = USER.objects.get(recno = recno)
            # except:
            #     raise Exception({'Success': success, 'Error': 'Not Found'})
            
            # schemes = request_data['schemes']
            # active = request_data.get('active', 1)

            # update = 'UPDATE test_table SET name = %s,email = %s, active = %s WHERE recno = %s'
            # with connection.cursor() as c:
            #     c.execute(update, [name,email,active,recno])

            update = f"UPDATE sensordata SET valuedata = '{valuedata}' WHERE recno = {recno}"
            with connection.cursor() as c:
                c.execute(update)
            success = True

            return Response({'Success': success, 'Message': 'Updated Successfully'}, status= 200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    """def delete(self, request):

        # success = False

        try:
            request_data = request.data
            recno = request_data['recno']

            delete = 'UPDATE test_table SET active = False WHERE recno = %s'

            with connection.cursor() as c:
                c.execute(delete, [recno])
            
            success = True
            return Response({'Success': success, 'Message': 'Deleted Successfully'}, status=200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : False, 'Error' : str(err)}, status=400) """

class SensorsCrud(APIView):

    def get(self,request,recno = None):

        success = False

        try:
            if recno:                       # it checks if any value passed in payload or not
                get = "SELECT * FROM sensors WHERE recno = %s "   # AND active = True"
                with connection.cursor() as c:
                    c.execute(get, [recno])
                    row = dictfetchall(c)
                success = True
            else:
                get = "SELECT * FROM sensors"      # WHERE active = True"
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)                       # write code for dictfetchall
                success = True

            return Response({'Success' : success, 'Message' : row}, status=200)

        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    def post(self,request):
        
        success = False
        try:
            request_data = request.data
            
            descn = request_data['descn']
            digital = request_data['digital']

            
            if descn != None:
                add = "INSERT INTO sensors (descn,digital) VALUES (%s, %s)"

                with connection.cursor() as c:
                    c.execute(add, [descn,digital])
                
                get = "SELECT * FROM sensors ORDER BY recno DESC LIMIT 1"
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)

                success = True

                return Response({'Success': success, 'Message': row}, status=200)
            
            else:

                return Response({'Success': success, 'Error': 'try again'}, status=400)
            
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    def patch(self, request):

        success = False
        try:
            request_data = request.data
            recno = request_data.get('recno',None)
            descn = request_data.get('descn')
            digital = request_data.get('digital')    
            

            update = f"UPDATE sensors SET descn = '{descn}',digital = '{digital}' WHERE recno = {recno}"
            with connection.cursor() as c:
                c.execute(update)
            success = True

            return Response({'Success': success, 'Message': 'Updated Successfully'}, status= 200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    """def delete(self, request):

        # success = False

        try:
            request_data = request.data
            recno = request_data['recno']

            delete = 'UPDATE test_table SET active = False WHERE recno = %s'

            with connection.cursor() as c:
                c.execute(delete, [recno])
            
            success = True
            return Response({'Success': success, 'Message': 'Deleted Successfully'}, status=200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : False, 'Error' : str(err)}, status=400) """

class SettingCRUD(APIView):

    def get(self,request,recno = None):

        success = False

        try:
            if recno:                       # it checks if any value passed in payload or not
                get = "SELECT * FROM setting WHERE recno = %s "   # AND active = True"
                with connection.cursor() as c:
                    c.execute(get, [recno])
                    row = dictfetchall(c)
                success = True
            else:
                get = "SELECT * FROM setting"      # WHERE active = True"
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)                       # write code for dictfetchall
                success = True

            return Response({'Success' : success, 'Message' : row}, status=200)

        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    def post(self,request):
        
        success = False
        try:
            request_data = request.data
            
            projectid = request_data['projectid']
            projectinfo = request_data['projectinfo']
            Domainexpert = request_data['Domainexpert']
            expertcontact = request_data['expertcontact']
            expertemail = request_data['expertemail']
            lifespan = request_data['lifespan']
            growlight = request_data['growlight']
            uv = request_data['uv']
            tempcontrol = request_data['tempcontrol']
            phcontrol = request_data['phcontrol']
            clockoperation = request_data['clockoperation']
            
            if projectid != None:
                add = "INSERT INTO setting (projectid,projectinfo,Domainexpert,expertcontact,expertemail,lifespan,growlight,uv,tempcontrol,phcontrol,clockoperation) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                with connection.cursor() as c:
                    c.execute(add, [projectid,projectinfo,Domainexpert,expertcontact,expertemail,lifespan,growlight,uv,tempcontrol,phcontrol,clockoperation])
                
                get = "SELECT * FROM setting ORDER BY recno DESC LIMIT 1"
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)

                success = True

                return Response({'Success': success, 'Message': row}, status=200)
            
            else:

                return Response({'Success': success, 'Error': 'try again'}, status=400)
            
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    def patch(self, request):

        success = False
        try:
            request_data = request.data
            
            recno = request_data.get('recno',None)
            projectid = request_data.get('projectid')
            projectinfo = request_data.get('projectinfo')    
            Domainexpert = request_data.get('Domainexpert')
            expertcontact = request_data.get('expertcontact')
            expertemail = request_data.get('expertemail')
            lifespan = request_data.get('lifespan')
            growlight = request_data.get('growlight')
            uv = request_data.get('uv')
            tempcontrol = request_data.get('tempcontrol')
            phcontrol = request_data.get('phcontrol')
            clockoperation = request_data.get('clockoperation')

            update = f"UPDATE setting SET projectid = '{projectid}',projectinfo = '{projectinfo}',Domainexpert = '{Domainexpert}',expertcontact = '{expertcontact}',expertemail = '{expertemail}',lifespan = '{lifespan}',growlight = '{growlight}',uv = '{uv}',tempcontrol = '{tempcontrol}',phcontrol = '{phcontrol}',clockoperation = '{clockoperation}' WHERE recno = {recno}"
            with connection.cursor() as c:
                c.execute(update)
            success = True

            return Response({'Success': success, 'Message': 'Updated Successfully'}, status= 200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    """def delete(self, request):

        # success = False

        try:
            request_data = request.data
            recno = request_data['recno']

            delete = 'UPDATE test_table SET active = False WHERE recno = %s'

            with connection.cursor() as c:
                c.execute(delete, [recno])
            
            success = True
            return Response({'Success': success, 'Message': 'Deleted Successfully'}, status=200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : False, 'Error' : str(err)}, status=400) """

class SitesCRUD(APIView):

    def get(self,request,recno = None):

        success = False

        try:
            if recno:                       # it checks if any value passed in payload or not
                get = "SELECT * FROM sites WHERE recno = %s "   # AND active = True"
                with connection.cursor() as c:
                    c.execute(get, [recno])
                    row = dictfetchall(c)
                success = True
            else:
                get = "SELECT * FROM sites"      # WHERE active = True"
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)                       # write code for dictfetchall
                success = True

            return Response({'Success' : success, 'Message' : row}, status=200)

        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    def post(self,request):
        
        success = False
        try:
            request_data = request.data
            
            projectid = request_data['projectid']
            tenant = request_data['tenant']
            descn = request_data['descn']
            location = request_data['location']
            IPaddress = request_data['IPaddress']
            status = request_data['status']
            
            
            if projectid != None:
                add = "INSERT INTO sites (projectid,tenant,descn,location,IPaddress,status) VALUES (%s, %s,%s,%s,%s,%s)"

                with connection.cursor() as c:
                    c.execute(add, [projectid,tenant,descn,location,IPaddress,status])
                
                get = "SELECT * FROM sites ORDER BY recno DESC LIMIT 1"
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)

                success = True

                return Response({'Success': success, 'Message': row}, status=200)
            
            else:

                return Response({'Success': success, 'Error': 'try again'}, status=400)
            
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    def patch(self, request):

        success = False
        try:
            request_data = request.data
            
            recno = request_data.get('recno',None)
            projectid = request_data.get('projectid')
            tenant = request_data.get('tenant')    
            descn = request_data.get('descn')
            location = request_data.get('location')
            IPaddress = request_data.get('IPaddress')
            status = request_data.get('status')

            update = f"UPDATE sites SET projectid = '{projectid}',tenant = '{tenant}',descn = '{descn}',location = '{location}',IPaddress = '{IPaddress}',status = '{status}' WHERE recno = {recno}"
            with connection.cursor() as c:
                c.execute(update)
            success = True

            return Response({'Success': success, 'Message': 'Updated Successfully'}, status= 200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    """def delete(self, request):

        # success = False

        try:
            request_data = request.data
            recno = request_data['recno']

            delete = 'UPDATE test_table SET active = False WHERE recno = %s'

            with connection.cursor() as c:
                c.execute(delete, [recno])
            
            success = True
            return Response({'Success': success, 'Message': 'Deleted Successfully'}, status=200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : False, 'Error' : str(err)}, status=400) """

class SitesensorsCRUD(APIView):

    def get(self,request,recno = None):

        success = False

        try:
            if recno:                       # it checks if any value passed in payload or not
                get = "SELECT * FROM sitesensors WHERE recno = %s "   # AND active = True"
                with connection.cursor() as c:
                    c.execute(get, [recno])
                    row = dictfetchall(c)
                success = True
            else:
                get = "SELECT * FROM sitesensors"      # WHERE active = True"
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)                       # write code for dictfetchall
                success = True

            return Response({'Success' : success, 'Message' : row}, status=200)

        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    def post(self,request):
        
        success = False
        try:
            request_data = request.data
            
            site = request_data['site']
            sensor = request_data['sensor']
            descn = request_data['descn']
            
            if site != None:
                add = "INSERT INTO sitesensors (site,sensor,descn) VALUES (%s,%s,%s)"

                with connection.cursor() as c:
                    c.execute(add, [site,sensor,descn])
                
                get = "SELECT * FROM sitesensors ORDER BY recno DESC LIMIT 1"
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)

                success = True

                return Response({'Success': success, 'Message': row}, status=200)
            
            else:

                return Response({'Success': success, 'Error': 'try again'}, status=400)
            
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    def patch(self, request):

        success = False
        try:
            request_data = request.data
            
            recno = request_data.get('recno',None)
            site = request_data.get('site')
            sensor = request_data.get('sensor')    
            descn = request_data.get('descn')

            update = f"UPDATE sitesensors SET site = '{site}',sensor = '{sensor}',descn = '{descn}' WHERE recno = {recno}"
            with connection.cursor() as c:
                c.execute(update)
            success = True

            return Response({'Success': success, 'Message': 'Updated Successfully'}, status= 200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    """def delete(self, request):

        # success = False

        try:
            request_data = request.data
            recno = request_data['recno']

            delete = 'UPDATE test_table SET active = False WHERE recno = %s'

            with connection.cursor() as c:
                c.execute(delete, [recno])
            
            success = True
            return Response({'Success': success, 'Message': 'Deleted Successfully'}, status=200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : False, 'Error' : str(err)}, status=400) """

class TenantCRUD(APIView):

    def get(self,request,recno = None):

        success = False

        try:
            if recno:                       # it checks if any value passed in payload or not
                get = "SELECT * FROM tenant WHERE recno = %s "   # AND active = True"
                with connection.cursor() as c:
                    c.execute(get, [recno])
                    row = dictfetchall(c)
                success = True
            else:
                get = "SELECT * FROM tenant"      # WHERE active = True"
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)                       # write code for dictfetchall
                success = True

            return Response({'Success' : success, 'Message' : row}, status=200)

        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    def post(self,request):
        
        success = False
        try:
            request_data = request.data
            
            tenantid = request_data['tenantid']
            descn = request_data['descn']
            
            if tenantid != None:
                add = "INSERT INTO tenant (tenantid,descn) VALUES (%s,%s)"

                with connection.cursor() as c:
                    c.execute(add, [tenantid,descn])
                
                get = "SELECT * FROM tenant ORDER BY recno DESC LIMIT 1"
                with connection.cursor() as c:
                    c.execute(get)
                    row = dictfetchall(c)

                success = True

                return Response({'Success': success, 'Message': row}, status=200)
            
            else:

                return Response({'Success': success, 'Error': 'try again'}, status=400)
            
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    def patch(self, request):

        success = False
        try:
            request_data = request.data
            
            recno = request_data.get('recno',None)
            tenantid = request_data.get('tenantid')
            descn = request_data.get('descn')

            update = f"UPDATE tenant SET tenantid = '{tenantid}',descn = '{descn}' WHERE recno = {recno}"
            with connection.cursor() as c:
                c.execute(update)
            success = True

            return Response({'Success': success, 'Message': 'Updated Successfully'}, status= 200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : success, 'Error' : str(err)}, status=400)

    """def delete(self, request):

        # success = False

        try:
            request_data = request.data
            recno = request_data['recno']

            delete = 'UPDATE test_table SET active = False WHERE recno = %s'

            with connection.cursor() as c:
                c.execute(delete, [recno])
            
            success = True
            return Response({'Success': success, 'Message': 'Deleted Successfully'}, status=200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success' : False, 'Error' : str(err)}, status=400) """

"""projectDir
    -settings.py
    -urls.py

appDir
    -appName1dir
        --models
        --serializer
        --views
        -urls
    -appName2dir
        --models
        --serializer
        --views
        -urls

    -utils.py

manage.py

docker
jenkins
conf"""