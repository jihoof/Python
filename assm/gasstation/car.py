from libs.module import clear
import random
import llm

class Car():
    def __init__(self, fuel_type, vehicle_type, capacity, unit):
        self.fuel_type = fuel_type
        self.vehicle_type = vehicle_type
        self.capacity = capacity
        self.cur_fuel = 0
        self.needed = 0
        self.full = False
        self.cal_fuel()
        self.unit = unit
    
    def cal_fuel(self):
        self.cur_fuel = int(self.capacity * random.uniform(0.1, 0.4))
        if random.randint(1, 4) == 1:
            self.full = True
            self.needed = self.capacity - self.cur_fuel
            
        else:
            self.full = False
            self.needed = ((self.capacity - self.cur_fuel) * random.uniform(0.5, 0.8) // 5) * 5
            

    def print_info(self):
        clear()
        self.make_json()
        answer = llm.llm_answer(f"""
            <<Vehicle Info>>
            {self.car_info}

            위 정보는 실제 차량 데이터다.
            너는 주유소 또는 전기차 충전소에서 직원에게 차량 상태를 설명하는 운전자다.

            아래 규칙을 반드시 지켜 답변하라.

            [핵심 규칙]
            1. 배터리 잔량(%)과 주행 가능 거리(km)는 절대 동일시하지 말 것
            2. 계산은 "최대 용량 기준 잔여 비율"로만 수행할 것
            3. km는 참고 정보로만 언급하고, 충전 필요량 계산에는 사용하지 말 것
            4. 감정 표현, 긴급 요청, 명령조 표현(예: 빨리, 최대한)은 사용 금지

            [출력 규칙]
            5. 공손하고 차분한 말투로 2~3문장 이내
            6. 차량 종류, 현재 잔량(%), 추가로 필요한 충전량(%), 연료 종류만 명확히 언급
            7. 추측, 과장, 해석 추가 금지
            8. 답변만 출력할 것

            답변을 생성하라.
            """
        )
        print(answer)

    def make_json(self):
        self.car_info = {
            'fuel_type': self.fuel_type,
            'vehicle_type': self.vehicle_type,
            'capacity': self.capacity,
            'cur_fuel': self.cur_fuel,
            'needed': self.needed,
            'full': self.full,
            "unit": self.unit
           }
        
    def fuel(self):
        pass

# 차량 종류
class Gasoline_Car(Car):
    def __init__(self, vehicle_type, capacity, unit):
        super.__init__("Gasoline", vehicle_type, capacity, unit)

class Diesel_Car(Car):
    def __init__(self, vehicle_type, capacity, unit):
        super.__init__("Diesel", vehicle_type, capacity, unit)

class Electric_Car(Car):
    def __init__(self,vehicle_type, capacity, unit):
        super().__init__("Electric", vehicle_type, capacity, unit)

# 가솔린 차량
class Hyundai_Avante(Gasoline_Car):
    def __init__(self):
        super().__init__("Hyundai Avante", 50, "L")   

class Toyota_Camry(Gasoline_Car):
    def __init__(self):
        super().__init__("Toyota Camry", 60, "L")

class Honda_Civic(Gasoline_Car):
    def __init__(self):
        super().__init__("Honda Civic", 45, "L")

# 디젤 차량
class Hyundai_Santa_Fe_Diesel(Diesel_Car):
    def __init__(self):
        super().__init__("Hyundai Santa Fe Diesel", 67, "L")

class Kia_Sorento_Diesel(Diesel_Car):
    def __init__(self):
        super().__init__("Kia Sorento Diesel", 78, "L")

class BMW_320d(Diesel_Car):
    def __init__(self):
        super().__init__("BMW 320d", 59, "L")


# 전기 차량
class Tesla_Model_3(Electric_Car):
    def __init__(self):
        super().__init__("Tesla Model 3", 62, "kWh")

class Tesla_Model_Y(Electric_Car):
    def __init__(self):
        super().__init__("Tesla Model Y", 90, "kWh")

class  Hyundai_Ioniq_5(Electric_Car):
    def __init__(self):
        super().__init__("Hyundai Ioniq 5", 77, "kWh")

# 이벤트 차량


