from flask import Flask


def first_come_first_serve(processes):
    start_time = 0
    end_time = 0
    ave_waiting_time = 0
    gantt_chart = {'sequence': list(processes)}
    gantt_chart['sequence'] = sorted(processes, key=itemgetter('arrival'))
    for item in gantt_chart['sequence']:
        end_time += int(item['burst'])
        ave_waiting_time += (start_time - int(item['arrival']))
        item['start_time'] = start_time
        item['end_time'] = end_time
        start_time = end_time
        item.pop('arrival', None)
    gantt_chart['ave_waiting_time'] = ave_waiting_time / float(len(processes))
    print(f'{gantt_chart}')
    return gantt_chart