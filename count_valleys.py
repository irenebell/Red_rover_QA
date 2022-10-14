def counting_valleys(s):
    count = 0
    level = 0
    is_valley = False
    for i in s:
        if i == "U":
            level += 1
        elif i == 'D':
            level -= 1
        if level < 0 and not is_valley:
            is_valley = True
        if level == 0 and is_valley:
            count += 1
            is_valley = False
    print(count)

counting_valleys('DFFU')


# bytes

# def user_friendly_size(b):
#     if b < 1000:
#     friendly = round(bytes / 1024, 2)
#     print(friendly)
#
# user_friendly_size(98967)
