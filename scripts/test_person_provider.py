import cv2

from tryon_service.providers.person.provider import (
    PersonDetectionProvider,
)

from tryon_service.services.person.person_detection_service import (
    PersonDetectionService,
)

IMAGE = "scripts/images/two.jpeg"

provider = PersonDetectionProvider()
provider.load()

service = PersonDetectionService(provider)

image = cv2.imread(IMAGE)

result = service.detect(image)

print("================================")
print("Detection Finished")
print("================================")

print("Persons:", result.person_count)

for detection in result.detections:

    print(detection)