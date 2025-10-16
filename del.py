
employye table
1. id (pk)
2. name varchar
3. salarie
4. depatment (fk)
5, craeted_at
6. update_at
7. is_deleted

class Employee(APIView):
    permission_calls = [IsValided]

    def post(self, request):
        data = request.data
        try:
            # json data converting to native python
            serializer = Empoyeeserializer(data) # save the or create serializer
            if serializer.is_valid():
                serializer.save()
        except Exception as e:
            return " Error occurs"

    def get(self, request):
        id = request.query_param.get('id')

        if not id:
            return "No id provided"

        try:
            if id:
                employee = Employee.objects.filter(id=id) | get(pk=id)
                employee = EmployeeSerilize(employee)
                resturn Response(employee.data)
            else:
                employee_list = Employee.objects.filter(is_deleted=False)

                employee_list = EmplyeeSerialiser(employee_list, many=True)
                resturn Response(employee_list.data)
        except Exception as e:
            return " Error occurs"

    def put(self, request):
        '''
        method: PUT
        sample json payload have to pass in body:
        {
            'id': 6,
            'salary': 78
        }
        :param request:  id : EMP ID, salary : specific Employee Salary
        :return:
         success:200 Ok Salary is updated
         error: 400 Employee Not Found
        '''

        id = request.body.get('id')
        salary = request.body.get('salary')

        if not id:
            return Response("No id provided" )

        if not salary:
            return Response("No salary provided")

        try:
            employee = Employee.objects.select_for_update(id=id)
            employee.salary = salary
            employee.save()
            return Response(f"salary of {salary}updated for employee  {id}")
        except Employee.DoesNotExist:
            return Response("Employee not found")



