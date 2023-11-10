import cv2
import numpy as np
from scipy import ndimage
import time


class Detector:
    def __init__(self, config=None, gaussian_blur=True, binary_fill_hole=True):
        self.gaussian_blur = gaussian_blur
        self.binary_fill_hole = binary_fill_hole
        if config is not None:
            if type(config) is not dict:
                raise ValueError("The config input must be dictionary type.")
            else:
                for key, value in config.items():
                    self.update_config_by_name(key, value)
        else:
            self.min_circular_ratio = 0.9
            self.max_circular_ratio = 1.9
            self.ksize_height = 13
            self.ksize_width = 13
            self.min_binary_threshold = 20
            self.max_binary_threshold = 255

    def update_config(self, config_dict_input):
        if type(config_dict_input) is not dict:
            raise ValueError("The config input must be dictionary type.")
        else:
            for key, value in config_dict_input.items():
                self.update_config_by_name(key, value)

    def update_config_by_name(self, attribute_name, attribute_value):
        if attribute_name == "min_circular_ratio":
            if type(attribute_value) is not float or type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be float or integer.")
            else:
                self.min_circular_ratio = round(float(attribute_value), 1)
        elif attribute_name == "max_circular_ratio":
            if type(attribute_value) is not float or type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be float or integer.")
            else:
                self.max_circular_ratio = round(float(attribute_value), 1)
        elif attribute_name == "ksize_height":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.ksize_height = attribute_value
        elif attribute_name == "ksize_width":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.ksize_width = attribute_value
        elif attribute_name == "min_binary_threshold":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.min_binary_threshold = attribute_value
        elif attribute_name == "max_binary_threshold":
            if type(attribute_value) is not int:
                raise ValueError(f"{attribute_name} must be integer.")
            else:
                self.max_binary_threshold = attribute_value
        else:
            print(f"Detector attribute type {attribute_name} could not find in detector attributes.")

    def get_config_info(self):
        temp_dict = {}
        temp_dict["min_circular_ratio"] = self.min_circular_ratio
        temp_dict["max_circular_ratio"] = self.max_circular_ratio
        temp_dict["ksize_height"] = self.ksize_height
        temp_dict["ksize_width"] = self.ksize_width
        temp_dict["min_binary_threshold"] = self.min_binary_threshold
        temp_dict["max_binary_threshold"] = self.max_binary_threshold
        return temp_dict

    def detect(self, frame_input):
        # Checking it is rbg/bgr image or not
        # If yes, then change to grayscale image
        if len(frame_input.shape) == 3:
            frame_input = cv2.cvtColor(frame_input, cv2.COLOR_BGR2GRAY)

        frame_shape = frame_input.shape
        frame_width = frame_shape[1]
        frame_height = frame_shape[0]

        if self.gaussian_blur:
            frame_input = cv2.GaussianBlur(frame_input, (self.ksize_height, self.ksize_width), 0)

        _, black_white_filter_frame = cv2.threshold(frame_input,
                                                    self.min_binary_threshold,
                                                    self.max_binary_threshold,
                                                    cv2.THRESH_BINARY_INV)

        if self.binary_fill_hole:
            binary_filled_frame = ndimage.binary_fill_holes(black_white_filter_frame).astype(np.uint8)
            binary_filled_frame[binary_filled_frame == 1] = 255
            try:
                contours, _ = cv2.findContours(binary_filled_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            except ValueError:
                contours = None
        else:
            try:
                contours, _ = cv2.findContours(black_white_filter_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            except ValueError:
                contours = None

        if contours is not None:
            contours = sorted(contours, key=lambda xx: cv2.contourArea(xx), reverse=True)

            min_circular_ratio = self.min_circular_ratio
            max_circular_ratio = self.max_circular_ratio
            largest_dia = 0.0
            largest_con_ind = 0
            error_string = None
            center_of_pupil = (0.0, 0.0)
            reversed_center_of_pupil = (0.0, 0.0)
            axes_of_pupil = (0.0, 0.0)
            average_diameter_of_pupil = 0.0
            angle_of_pupil = 0.0
            circular_con_count = 0
            for ind, cc in enumerate(contours):
                try:
                    (x, y), (MA, ma), angle = cv2.fitEllipse(cc)
                    con_ratio = ma / MA
                    # print(con_ratio)
                    if min_circular_ratio <= con_ratio <= max_circular_ratio:
                        avg_dia = (ma + MA) / 2
                        if avg_dia >= largest_dia:
                            largest_dia = avg_dia
                            largest_con_ind = ind
                            center_of_pupil = (float(x), float(y))
                            reversed_center_of_pupil = (float(frame_width - x), float(frame_height - y))
                            axes_of_pupil = (float(MA / 2), float(ma / 2))
                            average_diameter_of_pupil = avg_dia
                            angle_of_pupil = float(angle)
                            circular_con_count += 1
                except Exception as e:
                    error_string = str(e)
                    pass

            try:
                largest_circle = contours[largest_con_ind]
            except IndexError:
                largest_circle = None

            if largest_circle is not None:
                temp_dict = {}
                temp_dict["detector_timestamp"] = time.time()
                temp_dict["center_of_pupil"] = center_of_pupil
                temp_dict["reversed_center_of_pupil"] = reversed_center_of_pupil
                temp_dict["axes_of_pupil"] = axes_of_pupil
                temp_dict["angle_of_pupil"] = angle_of_pupil
                temp_dict["average_diameter_of_pupil"] = average_diameter_of_pupil
                return temp_dict
            else:
                temp_dict = {}
                temp_dict["detector_timestamp"] = time.time()
                temp_dict["center_of_pupil"] = (0.0, 0.0)
                temp_dict["reversed_center_of_pupil"] = (0.0, 0.0)
                temp_dict["axes_of_pupil"] = (0.0, 0.0)
                temp_dict["angle_of_pupil"] = 0.0
                temp_dict["average_diameter_of_pupil"] = 0.0
                return temp_dict
        else:
            temp_dict = {}
            temp_dict["detector_timestamp"] = time.time()
            temp_dict["center_of_pupil"] = (0.0, 0.0)
            temp_dict["reversed_center_of_pupil"] = (0.0, 0.0)
            temp_dict["axes_of_pupil"] = (0.0, 0.0)
            temp_dict["angle_of_pupil"] = 0.0
            temp_dict["average_diameter_of_pupil"] = 0.0
            return temp_dict


