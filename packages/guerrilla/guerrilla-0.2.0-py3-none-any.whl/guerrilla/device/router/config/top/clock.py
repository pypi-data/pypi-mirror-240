from typing import SupportsIndex, Union
from guerrilla.device.router.config import BaseConfig

class Clock(BaseConfig):
    
    def _validate_offset_hour(self, offset_hour: int) -> bool:
        if abs(offset_hour) > 12:
            self.device.logger.warning(f"Invalid offset hour: {offset_hour}, offset hour must be an integer between -12 and 12")
            return False
        return True
    
    def _validate_summer_time(self, month: Union[str, int], week:Union[str, int], day:Union[str, int], hh: SupportsIndex, mm: SupportsIndex) -> bool:
            """
            Validates the given month value.

            Args:
                month (Union[str, int]): The month value to validate. Can be either a string (e.g. 'jan', 'january') or an integer (1-12).

            Returns:
                bool: True if the month value is valid, False otherwise.
            """
            # Mapping of month names to their numeric values
            month_mapping = {
                'jan': 1, 'january': 1,
                'feb': 2, 'february': 2,
                'mar': 3, 'march': 3,
                'apr': 4, 'april': 4,
                'may': 5,
                'jun': 6, 'june': 6,
                'jul': 7, 'july': 7,
                'aug': 8, 'august': 8,
                'sep': 9, 'september': 9,
                'oct': 10, 'october': 10,
                'nov': 11, 'november': 11,
                'dec': 12, 'december': 12
            }

            # Check month and convert if necessary
            if isinstance(month, str):
                month = month_mapping.get(month.lower())
                if month is None:
                    self.device.logger.warning(f"Invalid month: {month}, month must be a string or integer between 1-12")
                    return False
            elif not isinstance(month, int) or abs(month) > 12:
                self.device.logger.warning(f"Invalid month: {month}, month must be a string or integer between 1-12")
                return False
            # Check week and convert if necessary, From '1st' or '1' to 'Last' or '6'
            week_mapping = {
                '1st': 1, '1': 1,
                '2nd': 2, '2': 2,
                '3rd': 3, '3': 3,
                '4th': 4, '4': 4,
                '5th': 5, '5': 5,
                'last': 6, '6': 6
            }
            if isinstance(week, str):
                week = week_mapping.get(week.lower())
                if week is None:
                    self.device.logger.warning(f"Invalid week: {week}, week must be a string or integer between 1-6")
                    return False
            elif not isinstance(week, int) or abs(week) > 6:
                self.device.logger.warning(f"Invalid week: {week}, week must be a string or integer between 1-6")
                return False
            
            # Check day and convert if necessary, From 'Sun', 'Sunday' or '1' to 'Sat', 'Saturday' or '7'
            day_mapping = {
                'sun': 1, 'sunday': 1, '1': 1,
                'mon': 2, 'monday': 2, '2': 2,
                'tue': 3, 'tuesday': 3, '3': 3,
                'wed': 4, 'wednesday': 4, '4': 4,
                'thu': 5, 'thursday': 5, '5': 5,
                'fri': 6, 'friday': 6, '6': 6,
                'sat': 7, 'saturday': 7, '7': 7
            }
            if isinstance(day, str):
                day = day_mapping.get(day.lower())
                if day is None:
                    self.device.logger.warning(f"Invalid day: {day}, day must be a string or integer between 1-7")
                    return False
            elif not isinstance(day, int) or abs(day) > 7:
                self.device.logger.warning(f"Invalid day: {day}, day must be a string or integer between 1-7")
                return False
            
            # Check hour and convert if necessary
            if not isinstance(hh, int) or abs(hh) > 23:
                self.device.logger.warning(f"Invalid hour: {hh}, hour must be an integer between 0-23")
                return False
            
            # Check minute and convert if necessary
            if not isinstance(mm, int) or abs(mm) > 59:
                self.device.logger.warning(f"Invalid minute: {mm}, minute must be an integer between 0-59")
                return False
                
            
            return True
    
    def set_clock(self, year: SupportsIndex, month: SupportsIndex, day: SupportsIndex, hh: SupportsIndex, mm: SupportsIndex, ss: SupportsIndex):
        """
        Sets the clock of the router device to the specified date and time.

        Args:
            year (int): The year.
            month (int): The month.
            day (int): The day.
            hh (int): The hour.
            mm (int): The minute.
            ss (int): The second.
        """

        self._execute_config_command(f'clock set {hh}:{mm}:{ss} {month} {day} {year}', 
                                        success_message=f"Clock set to {hh}:{mm}:{ss} {month} {day} {year}")
        
    def set_timezone(self,offset_hour: int):
        """
        Sets the timezone of the router device to the specified offset hour.

        Args:
            offset_hour (int): The offset hour.
        """
        if self._validate_offset_hour(offset_hour):
            with self.setting_config():
                self.device.run(f'clock timezone gmt {offset_hour}')
                self.device.logger.success(f"Timezone set to {offset_hour}")
            
    def set_summer_time_start(self, month: Union[str, int], week:Union[str, int], day:Union[str, int], hh: SupportsIndex, mm: SupportsIndex):
        """
        Sets the start of the summer time based on the month provided.
        The month can be a string like 'Jan', 'January', or an integer 1-12.
        """
        if self._validate_summer_time(month, week, day, hh, mm):
            with self.setting_config():
                self.device.run(f'clock summer-time start-date {month} {week} {day} {hh}:{mm}')
                self.device.logger.success(f"Summer time start set to {month} {week} {day} {hh}:{mm}")
            
    def set_summer_time_end(self, month: Union[str, int], week:Union[str, int], day:Union[str, int], hh: SupportsIndex, mm: SupportsIndex):
        """
        Sets the end of the summer time based on the month provided.
        The month can be a string like 'Jan', 'January', or an integer 1-12.
        """
        if self._validate_summer_time(month, week, day, hh, mm):
            with self.setting_config():
                self.device.run(f'clock summer-time end-date {month} {week} {day} {hh}:{mm}')
                self.device.logger.success(f"Summer time end set to {month} {week} {day} {hh}:{mm}")
                
    def set_summer_time_offset(self, offset_hour: int):
        """
        Sets the summer time offset hour.
        """
        if self._validate_offset_hour(offset_hour):
            with self.setting_config():
                output = self.device.run(f'clock summer-time offset {offset_hour}')
                if "Please input the correct start/end date of the summer time first!" in output:
                    self.device.logger.warning("Please input the correct start/end date of the summer time first!")
                    return
                self.device.logger.success(f"Summer time offset set to {offset_hour}")