def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees

    parking = {}
    total_time = {}

    for record in records:
        record_time, car_number, status = record.split()

        hour, minute = map(int, record_time.split(":"))
        current_time = hour * 60 + minute

        if status == "IN":
            parking[car_number] = current_time

        else:
            in_time = parking.pop(car_number)
            parked_time = current_time - in_time

            if car_number not in total_time:
                total_time[car_number] = 0

            total_time[car_number] += parked_time

    # 출차하지 않은 차량은 23:59에 출차
    end_time = 23 * 60 + 59

    for car_number, in_time in parking.items():
        if car_number not in total_time:
            total_time[car_number] = 0

        total_time[car_number] += end_time - in_time

    answer = []

    # 차량 번호순으로 요금 계산
    for car_number in sorted(total_time):
        parked_time = total_time[car_number]

        if parked_time <= base_time:
            fee = base_fee
        else:
            extra_time = parked_time - base_time

            # 단위 시간으로 나누어 올림
            count = (extra_time + unit_time - 1) // unit_time
            fee = base_fee + count * unit_fee

        answer.append(fee)

    return answer