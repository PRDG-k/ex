from abc import ABC, abstractmethod

class ElectricityData(ABC):
    def __init__(self, usage_data: list):
        self.__usage_data = usage_data
        if self.usage_data:
            self.__total_usage = self.calculate_total_usage()
        else:
            self.__total_usage = 0
    
    def __str__(self):
        return f"총 전력 사용량: {self.total_usage:.2f}"

    @property
    def usage_data(self):
        return self.__usage_data
    
    @usage_data.setter
    def usage_data(self, data: list):
        self.__usage_data = data
        if self.usage_data:
            self.total_usage = self.calculate_total_usage()
    
    @property
    def total_usage(self):
        return self.__total_usage
    
    @total_usage.setter
    def total_usage(self, usage: float):
        self.__total_usage = usage

    @abstractmethod
    def calculate_total_usage(self):
        pass
    
    @abstractmethod
    def get_usage_on_date(self, date):
        pass

    def add_usage(self, date, usage):
        for data in self.usage_data:
            if data["date"] == date:
                data["usage"] = usage
                print(f"{date}의 사용량을 {usage}로 수정했습니다.")
                print(f"{date} 수정 후 총 전력 사용량 {self.total_usage:.2f}")
                return
        
        self.usage_data.append({"date": date, "usage": usage})
        print(f"{date} 추가 후 총 전력 사용량 {self.total_usage:.2f}")
        self.total_usage = self.calculate_total_usage()
    
    def remove_usage(self, date):
        for data in self.usage_data:
            if data["date"] == date:
                self.usage_data.remove(data)
                break

class HomeElectricityData(ElectricityData):
    def calculate_total_usage(self):
        total = 0
        for data in self.usage_data:
            total += data["usage"]
        return total
    
    def get_usage_on_date(self, date):
        for data in self.usage_data:
            if data["date"] == date:
                print(f"{date}의 사용량: {data["usage"]}")
                return
            
        print(f"{date}의 사용량이 없습니다.")
    
    @classmethod
    def filter_by_date(cls, usage_date, start_date, end_date):
        filtered = []
        for data in usage_date:
            if start_date <= data["date"] and data["date"] <= end_date:
                filtered.append(data)
        return filtered
    
    # def filter_by_date(self, start_date, end_date):
    #     filtered = []
    #     for data in self.usage_data:
    #         if start_date <= data["date"] and data["date"] <= end_date:
    #             filtered.append(data)
    #     return filtered
    
    @staticmethod
    def get_max_usage(usage_data):
        filtered = []
        for data in usage_data:
            if data["usage"] == max(usage_data, key=lambda x: x["usage"])["usage"]:
                filtered.append(data)
                return filtered

electricity_usage = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6},
]

home_electricity = HomeElectricityData(electricity_usage)
print(home_electricity)
home_electricity.get_usage_on_date("2024-11-03")
home_electricity.add_usage("2024-11-06", 20)
print(f"특정 날짜 범위 내 사용량: {HomeElectricityData.filter_by_date(home_electricity.usage_data, "2024-11-02", "2024-11-04")}")
print(f"가장 높은 사용량: {home_electricity.get_max_usage(home_electricity.usage_data)}")