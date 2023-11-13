from pathlib import Path
from typing import Any

from nudenet import NudeDetector  # type:ignore

from ultima_scraper_detector.gui import Gui


class UltimaScraperDetector:
    def __init__(self, gui: bool = False):
        """
        Initializes an UltimaDetector instance.

        Args:
            gui (bool): Indicates whether a graphical user interface (GUI) should be used for displaying results.
        """
        self.nude_detector = NudeDetector()
        self.detections: dict[str, list[dict[str, Any]]] = {}
        self.gui = Gui() if gui else None

    def detect(self, filepath: Path, watch_keyword: str | None = None):
        """
        Detects and analyzes media content for explicit content using a nude detection module.

        Args:
            filepath (Path): The path to the media file to be analyzed.
            watch_keyword (str | None): A keyword to watch for in the detected content.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries representing detected media content,
            each containing information such as class and confidence level.
        """
        filepath_string = filepath.as_posix()
        media_detections: list[dict[str, Any]] = []
        try:
            media_detections.extend(
                self.nude_detector.detect(  # type:ignore
                    filepath_string
                )
            )
            self.detections[filepath.stem] = media_detections
        except AttributeError as _e:
            return media_detections
        if self.gui:
            if watch_keyword:
                has_keyword = any(
                    watch_keyword.lower() in item["class"].lower()
                    for item in media_detections
                )
                if has_keyword:
                    self.gui.update_image(filepath, media_detections)
            else:
                self.gui.update_image(filepath, media_detections)
        return media_detections

    def predict_sex(self):
        """
        Predicts the overall gender based on the detected classes in media content.

        Returns:
            str: The predicted overall gender, which can be "MALE," "FEMALE," or "UNKNOWN."
        """
        detections = self.detections.values()
        # Count the occurrences of female-related classes and male-related classes
        male_detections = [
            detection
            for detections_list in detections
            for detection in detections_list
            if "MALE" in detection["class"] and "FEMALE" not in detection["class"]
        ]
        female_detections = [
            detection
            for detections_list in detections
            for detection in detections_list
            if "FEMALE" in detection["class"]
        ]

        male_count = len(male_detections)
        female_count = len(female_detections)

        # Determine overall gender based on the counts
        if female_count > male_count:
            overall_gender = "FEMALE"
        elif male_count > female_count:
            overall_gender = "MALE"
        else:
            overall_gender = "UNKNOWN"
        return overall_gender
