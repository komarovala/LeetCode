#https://leetcode.com/problems/defanging-an-ip-address/

address = " "

def replace(address):
    address = address.replace(".", "[.]")
    return address


print(replace(address))