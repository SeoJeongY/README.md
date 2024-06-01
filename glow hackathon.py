def check_weight_status(sensor_reading, registered_weight):
    """
    압전소자를 사용하여 측정된 압력을 기준으로 몸무게의 상태를 확인하는 함수
    
    :param sensor_reading: 압전소자에서 측정된 압력 (float)
    :param registered_weight: 전동킥보드 앱에 등록된 사용자의 몸무게 (float)
    :return: 몸무게 상태 ("high", "low", "normal") (str)
    """
    
    
    threshold_factor_high = 1.5  
    threshold_factor_low = 0.7   
     
    # 임계값 계산
    weight_threshold_high = registered_weight * threshold_factor_high
    weight_threshold_low = registered_weight * threshold_factor_low
    
    
    if sensor_reading >= weight_threshold_high:
        return "high"
    elif sensor_reading <= weight_threshold_low:
        return "low"
    else:
        return "normal"

def calculate_penalty(start_time, current_time):
    """
    경고음이 울린 후부터 현재까지의 시간을 기반으로 벌금을 계산하는 함수
    
    :param start_time: 경고음이 울리기 시작한 시간 (초 단위) (float)
    :param current_time: 현재 시간 (초 단위) (float)
    :return: 벌금 (원) (float)
    """
    
    # 경과 시간 계산 (초 단위)
    elapsed_time = current_time - start_time
    
    # 경과 시간이 10초 이하이면 벌금 없음
    if elapsed_time <= 10:
        penalty = 0
    else:
        # 경과 시간이 10초를 초과한 경우 벌금 계산
        penalty = (elapsed_time - 10) * 500
    
    return penalty

# 사용자로부터 입력 받기
try:
    registered_weight = float(input("전동킥보드 앱에 등록된 사용자의 몸무게를 입력하세요 (kg): "))
    sensor_reading = float(input("압전소자에서 측정된 압력을 입력하세요: "))
    
    # 몸무게 상태 확인 함수 호출
    weight_status = check_weight_status(sensor_reading, registered_weight)
    
    
    if weight_status == "high" or weight_status == "low":
        print("주의: 몸무게가 정상 범위를 벗어났습니다. 경고음이 울립니다!")
        
        
        start_time = float(input("경고음이 울린 시간을 입력하세요 (초): "))
        current_time = float(input("현재 시간을 입력하세요 (초): "))
        
        # 경과 시간 계산
        elapsed_time = current_time - start_time
        
        
        if elapsed_time > 10:
            print("경고음이 10초 이상 울렸습니다. 추가 조치가 필요합니다.")
            
            # 벌금 계산 함수 호출
            penalty_amount = calculate_penalty(start_time, current_time)
            print("경고음이 울린 후 경과 시간: {:.2f}초".format(elapsed_time))
            print("벌금: {} 원".format(penalty_amount))
        else:
            print("경고음이 10초 이하로 울렸습니다. 벌금이 없습니다.")
    else:
        print("안전: 몸무게가 정상 범위 내에 있습니다. 킥보드를 작동합니다.")
except ValueError:
    print("잘못된 입력입니다. 숫자를 입력해주세요.")


