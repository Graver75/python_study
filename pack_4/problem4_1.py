trades_dict = {'V': [], 'D': [], 'X': [], 'Y': [], 'B': [], 'J': [], 'Q': [], 'Z': [], 'K': [], 'P': [], 'All': []}
max_dict = {'V': 0, 'D': 0, 'X': 0, 'Y': 0, 'B': 0, 'J': 0, 'Q': 0, 'Z': 0, 'K': 0, 'P': 0, 'All': 0}
times_dict = {'V': 0, 'D': 0, 'X': 0, 'Y': 0, 'B': 0, 'J': 0, 'Q': 0, 'Z': 0, 'K': 0, 'P': 0, 'All': 0}


def str_time_to_seconds(time):
    time_list = time.split(':')
    return float(time_list.pop()) + int(time_list.pop()) * 60 + int(time_list.pop()) * 3600


def seconds_to_str_time(time):
    zero_minutes = ''
    zero_hours = ''
    zero_seconds = ''
    hour = int(time // 3600)
    time -= hour * 3600
    minutes = int(time // 60)
    seconds = int((time - minutes * 60) * 1000) / 1000
    if hour < 10:
        zero_hours = '0'
    if minutes < 10:
        zero_minutes = '0'
    if seconds < 10:
        zero_seconds = '0'
    return zero_hours + str(hour) + ':' + zero_minutes + str(minutes) + ':' + zero_seconds + str(seconds)


def parse_cell(line_table):
    list_line = line_table.split(',')
    time = str_time_to_seconds(list_line[0])
    exchange = list_line[3][0]
    append_trade(time, exchange)


def append_trade(time, exchange):
    trades_dict[exchange].append(time)
    while time - trades_dict[exchange][0] >= 1:
        trades_dict[exchange].pop(0)
    if len(trades_dict[exchange]) > max_dict[exchange]:
        max_dict[exchange] = len(trades_dict[exchange])
        times_dict[exchange] = trades_dict[exchange][0]
    if exchange != 'All':
        exchange = 'All'
        append_trade(time, exchange)


def output():
    print('Once going through the table, once checking for the dictionaries')
    print('Complexity: O(n)')
    for a in max_dict:
        space = '  '
        if a == 'All':
            space = ''
        print(a + ':', space + str(max_dict[a]), ' ' * (4 - len(str(max_dict[a])))
              + seconds_to_str_time(times_dict[a]))


with open("TRD2.csv") as f:
    f.readline()
    for line in f.readlines():
        parse_cell(line)

output()
