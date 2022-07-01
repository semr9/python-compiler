from rest_framework.decorators import api_view
from django.http.response import JsonResponse
import subprocess
import datetime
import sys
from rest_framework.parsers import JSONParser


@api_view(['GET'])
def serverDateApi(request):
    if request.method == 'GET':
        date = datetime.datetime.now()
        return JsonResponse({"date": date}, safe=False)


@api_view(['POST'])
def executeCode(request):
    if request.method == 'POST':
        # Expected code {'code':'',input:''}
        input_data = JSONParser().parse(request)
        code = input_data['code']
        input = input_data['input']

        with open("code.py", "w") as text_file:  # Create file for exec
            n = text_file.write(code)

        code_lines = code.split('\n')
        # print("code_lines:", code_lines)

        input_numbers = 0
        for line in code_lines:
            if line.find('input'):
                input_numbers += 1

        input = input[:input_numbers]  # Get only necessary input lines
        input = ('\n'.join([str(input_) for input_ in input])).encode()

        cmd = ["python", "code.py"]
        try:
            # run python file
            res = subprocess.run(cmd, input=input, capture_output=True)

            output = res.stdout.decode()
            if res.returncode != 0:  # error
                error = res.stdout.decode()
                response = "Error Code: " + str(res.returncode)
                response += "Error Message: " + str(error)
                response += "Code output: " + str(output)
                print('Error Code: ', res.returncode)
                print('Error Message: ', error)
                return JsonResponse(response, safe=False)

        except OSError as e:
            print("Error: Error from OS. Return Code = ", e.errno)
            print("Error Message: ", e.strerror)
            response = "Error: Error from OS. Return Code = " + str(e.errno)
            response += "Error Message: " + str(e.strerror)
            return JsonResponse(response, safe=False)
        except:
            print("Error: Error on System Execution : ", sys.exc_info())
            response = "Error: Error on System Execution : " + str(
                sys.exc_info())
            return JsonResponse(response, safe=False)

        # print("all good, output:")
        # print(output)
        return JsonResponse(output, safe=False)
