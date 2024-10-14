import cv2
import os

# Hindi letters from अ to ज्ञ
hindi_letters = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ', 'अं', 'अः',
                 'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ',
                 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'क्ष', 'त्र', 'ज्ञ','blank']

directory = 'HindiSignImages48x48/'

# Create directories for each Hindi letter if not exist
if not os.path.exists(directory):
    os.mkdir(directory)

for letter in hindi_letters:
    if not os.path.exists(f'{directory}/{letter}'):
        os.mkdir(f'{directory}/{letter}')

# Open webcam and start capturing images
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # Dictionary to keep count of images in each folder
    count = {letter: len(os.listdir(directory + "/" + letter)) for letter in hindi_letters}

    # Show live frame and capture the region of interest (ROI)
    row, col = frame.shape[1], frame.shape[0]
    cv2.rectangle(frame, (0, 40), (300, 300), (255, 255, 255), 2)
    cv2.imshow("data", frame)
    frame = frame[40:300, 0:300]
    cv2.imshow("ROI", frame)

    # Convert ROI to grayscale and resize
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (48, 48))

    # Capture key input and save the corresponding frame for each Hindi letter
    interrupt = cv2.waitKey(10)

    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(os.path.join(directory + 'अ/' + str(count['अ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(os.path.join(directory + 'आ/' + str(count['आ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(os.path.join(directory + 'इ/' + str(count['इ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(os.path.join(directory + 'ई/' + str(count['ई']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(os.path.join(directory + 'उ/' + str(count['उ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(os.path.join(directory + 'ऊ/' + str(count['ऊ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(os.path.join(directory + 'ए/' + str(count['ए']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(os.path.join(directory + 'ऐ/' + str(count['ऐ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('9'):
        cv2.imwrite(os.path.join(directory + 'ओ/' + str(count['ओ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(os.path.join(directory + 'औ/' + str(count['औ']) + '.jpg'), frame)

    # Continue the same pattern for the rest of the Hindi letters
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(os.path.join(directory + 'अं/' + str(count['अं']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(os.path.join(directory + 'अः/' + str(count['अः']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(os.path.join(directory + 'क/' + str(count['क']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(os.path.join(directory + 'ख/' + str(count['ख']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(os.path.join(directory + 'ग/' + str(count['ग']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(os.path.join(directory + 'घ/' + str(count['घ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(os.path.join(directory + 'ङ/' + str(count['ङ']) + '.jpg'), frame)

    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(os.path.join(directory + 'ज/' + str(count['ज']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(os.path.join(directory + 'झ/' + str(count['झ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(os.path.join(directory + 'ञ/' + str(count['ञ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(os.path.join(directory + 'ट/' + str(count['ट']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(os.path.join(directory + 'ठ/' + str(count['ठ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(os.path.join(directory + 'ड/' + str(count['ड']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(os.path.join(directory + 'ढ/' + str(count['ढ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(os.path.join(directory + 'ण/' + str(count['ण']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(os.path.join(directory + 'त/' + str(count['त']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(os.path.join(directory + 'थ/' + str(count['थ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(os.path.join(directory + 'द/' + str(count['द']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(os.path.join(directory + 'ध/' + str(count['ध']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(os.path.join(directory + 'न/' + str(count['न']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(os.path.join(directory + 'प/' + str(count['प']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(os.path.join(directory + 'फ/' + str(count['फ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(os.path.join(directory + 'ब/' + str(count['ब']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(os.path.join(directory + 'भ/' + str(count['भ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(os.path.join(directory + 'म/' + str(count['म']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(os.path.join(directory + 'य/' + str(count['य']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('!'):
        cv2.imwrite(os.path.join(directory + 'र/' + str(count['र']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('@'):
        cv2.imwrite(os.path.join(directory + 'ल/' + str(count['ल']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('#'):
        cv2.imwrite(os.path.join(directory + 'व/' + str(count['व']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('$'):
        cv2.imwrite(os.path.join(directory + 'श/' + str(count['श']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('%'):
        cv2.imwrite(os.path.join(directory + 'ष/' + str(count['ष']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('^'):
        cv2.imwrite(os.path.join(directory + 'स/' + str(count['स']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('&'):
        cv2.imwrite(os.path.join(directory + 'ह/' + str(count['ह']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('*'):
        cv2.imwrite(os.path.join(directory + 'क्ष/' + str(count['क्ष']) + '.jpg'), frame)
    if interrupt & 0xFF == ord('('):
        cv2.imwrite(os.path.join(directory + 'त्र/' + str(count['त्र']) + '.jpg'), frame)
    if interrupt & 0xFF == ord(')'):
        cv2.imwrite(os.path.join(directory + 'ज्ञ/' + str(count['ज्ञ']) + '.jpg'), frame)
    if interrupt & 0xFF == ord(' '):
        cv2.imwrite(os.path.join(directory + 'blank/' + str(count['blank']) + '.jpg'), frame)


    # Exit the loop with 'esc' key
    if interrupt & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
