from django import template
import math

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def divide(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0

@register.filter
def divisibleby(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0

@register.filter
def format_large_number(value):
    try:
        value = float(value)
        if value == 0:
            return "0"
        
        miles_millones = value / 1_000_000_000  # 9 ceros
        millones = value / 1_000_000  # 6 ceros
        
        if miles_millones >= 1:
            # Para números mayores o iguales a mil millones
            miles_millones_str = '{:,.0f}'.format(miles_millones).replace(',', '.')
            return f"{miles_millones_str} Mil Millones"
        
        if millones >= 1:
            # Para números mayores o iguales a un millón
            millones_str = '{:,.0f}'.format(millones).replace(',', '.')
            return f"{millones_str} Millones"
            
        # Para números menores a un millón
        return '{:,.0f}'.format(value).replace(',', '.')
            
    except (ValueError, TypeError):
        return "0"