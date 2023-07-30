import pandas as pd
import requests

arr_url=[
'paBkbufBFTQBsfWkPJFvzA%3D%3D',
'wCcn7gPWS%252BccdYFGwkYbEQ%253D%253D',
'JIiy0pXLc4BxBHuhMFKzMg%3D%3D',
'50sNVIfVFw%2B%2BpEQk8kfQCA%3D%3D',
'u6fk7PJ0d4n5mYqvt0GsXQ%3D%3D',
'X1%2BcvIGnmzo8MdQIsPZO4Q%3D%3D',
'eTusNJkJ8ZfPktZmur3Qig%253D%253D',
'7pyMqmMhoUhjKhAQhD0lFA%3D%3D',
'Uv7CQzO0fu9SPFdR7mwHiw',
'UjezdLmxiU8nq2EG9%2FL9KA%3D%3D',
'4nouBNAPaQtdxLMFkTO%2BNw%3D%3D',
'6vC5V46kUwPAOkkHPEp2Iw%3D%3D',
'W8fxmtx6kJaBYjHrSxJ9dw%3D%3D',
'C4HIq6hx3B%2FRSg2u7NeYJw%3D%3D',
'kBlvHJaYGeDpjiN7%2F0QUxA%3D%3D',
'3Xc5XRMNmeVFHJ%2BL276HRA%3D%3D',
'Y0gmyQjuuT4x4XKnYXOUow%3D%3D',
'GJIwbGttIGQBFTg4IXyAew%3D%3D',
'wwhIWlT6h3QyFG9qmTZsaA%3D%3D'
]
start="https://www.mca.gov.in/bin/dms/getdocument?mds="
end='&type=download'
# flag=str(input('Enter the format for data extraction: \n 0:y.Consolidated\n 2:Individual Files '))
print('> Choose a format for data extraction: \n  1.Consolidated\n  2.Individual Files')
flag=int(input())
type(flag)



if flag==1:
    consolidated=pd.DataFrame()
    for i in range(0,19):
        url=start+str(arr_url[i])+end
        data=requests.get(url)
        output = open('test.xlsx', 'ab')
        output.write(data.content)
        output.close()
        test=pd.read_excel(output)
        consolidated=consolidated.append(test)

    consolidated.to_csv('Consolidated.csv')


elif flag==2:

      def indivi():
            url=start+str(arr_url[0])+end
            data=requests.get(url)
            output = open('2022_December.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[1])+end
            data=requests.get(url)
            output = open('2022_November.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[2])+end
            data=requests.get(url)
            output = open('2022_October.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[3])+end
            data=requests.get(url)
            output = open('2022_September.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[4])+end
            data=requests.get(url)
            output = open('2022_August.xlsx', 'wb')
            output.write(data.content)
            output.close()
            
            url=start+str(arr_url[5])+end
            data=requests.get(url)
            output = open('2022_July.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[6])+end
            data=requests.get(url)
            output = open('2022_June.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[7])+end
            data=requests.get(url)
            output = open('2022_May.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[8])+end
            data=requests.get(url)
            output = open('2022_April.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[9])+end
            data=requests.get(url)
            output = open('2022_Febuary.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[10])+end
            data=requests.get(url)
            output = open('2022_January.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[11])+end
            data=requests.get(url)
            output = open('2021_October.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[12])+end
            data=requests.get(url)
            output = open('2021_September.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[13])+end
            data=requests.get(url)
            output = open('2021_August.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[14])+end
            data=requests.get(url)
            output = open('2021_July.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[15])+end
            data=requests.get(url)
            output = open('2021_June.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[16])+end
            data=requests.get(url)
            output = open('2021_May.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[17])+end
            data=requests.get(url)
            output = open('2021_April.xlsx', 'wb')
            output.write(data.content)
            output.close()

            url=start+str(arr_url[18])+end
            data=requests.get(url)
            output = open('2021_March.xlsx', 'wb')
            output.write(data.content)
            output.close()

print('!!!EXTRACTION SUCCESSFUL!!!')