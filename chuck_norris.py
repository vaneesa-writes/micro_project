import requests,json
next=True
while(next):
    out=""
    id = int(input("Enter a numver : "))
    response = requests.get(f"http://api.icndb.com/jokes/{id}")
    var = json.loads(response.content)
    try:
        print(var['value']['joke'])
        out=var['value']['joke']
    except:
        print("Try another number")
        out="Try another number"
    with open("chucknorrisjokes.csv","a",encoding="utf-8") as chuck:
        to_write=",".join([str(id),out])
        to_write+='\n'
        chuck.write(to_write)
    con=input("Enter Y to continue N to quit : ")
    if(con=='N' or con=='n' or con=='0'):
        next=False