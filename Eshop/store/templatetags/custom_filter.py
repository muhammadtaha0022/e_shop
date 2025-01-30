from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "₨ "+str(number)




# @register.filter(name='multiply')
# def multiply (number,number1):
#     return number * number1 


@register.filter(name='multiply')
def multiply(number, number1):
    if isinstance(number, (int, float)) and isinstance(number1, (int, float)):
        return number * number1
    return 0