import cv2

class Guide(object):
    def __init__(self, name, img):
        
        self.name = name
        
        self.img = img
        self.img_Y, self.img_X, _ = img.shape
        self.rect_img = self.img.copy()
        self.temp_img = None
        self.point_toggle = False
        self.drawing_toggle = False
        self.roi = None
        
        self.red = (0, 0, 255)
        self.green = (0, 255, 0)
        self.blue = (255, 0, 0)
        
        self.minX, self.minY, self.maxX, self.maxY, self.aX, self.aY, self.bX, self.bY = -1, -1, -1, -1, -1, -1, -1, -1
        
        cv2.namedWindow(self.name, cv2.WND_PROP_FULLSCREEN)
        cv2.setMouseCallback(self.name, self.draw_box, param=self.rect_img)
        while True:
            cv2.imshow(self.name, self.rect_img)
            
            input_key = cv2.waitKey(20) & 0xFF
            if input_key == 27:
                break
            
                
                
            elif input_key == ord('a') and self.point_toggle == False:
                print('X')
                self.roi = cv2.rectangle(self.rect_img, (self.minX, self.minY), (self.maxX, self.maxY), (0, 255, 0), 4)
                print(self.minX, self.minY, self.maxX, self.maxY)
            
            elif input_key == ord('b'):
                break
    cv2.destroyAllWindows()
        
    def init_rect(self):
        return self.minX, self.minY, self.maxX, self.maxY
    
    def draw_box(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing_toggle = True
            
            cv2.imshow(self.name, self.rect_img)
            if self.point_toggle is False:
                self.rect_img = self.img.copy()
                self.aX, self.aY = x, y
            else:
                self.bX, self.bY = x, y
        
        elif event == cv2.EVENT_MOUSEMOVE and self.drawing_toggle:           
            if self.drawing_toggle:
                if self.point_toggle is False:
                    self.rect_img = self.img.copy()
                    cv2.circle(self.rect_img, (x, y), 6, self.red, 2)
                    cv2.line(self.rect_img, (x, y), (self.img_X, y), self.red, 3)
                    cv2.line(self.rect_img, (x, y), (x, self.img_Y), self.red, 3)
                    self.temp_img = self.rect_img.copy()
                
                else:
                    self.rect_img = self.temp_img.copy()
                    cv2.circle(self.rect_img, (x, y), 6, self.blue, 2)
                    cv2.line(self.rect_img, (0, y), (x, y), self.blue, 3)
                    cv2.line(self.rect_img, (x, 0), (x, y), self.blue, 3)
        
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing_toggle = False
            if self.point_toggle is False:
                cv2.circle(self.rect_img, (x, y), 6, self.red, 2)
                cv2.line(self.rect_img, (x, y), (self.img_X, y), self.red, 3)
                cv2.line(self.rect_img, (x, y), (x, self.img_Y), self.red, 3)
                self.point_toggle = True
                
                self.aX, self.aY = x, y
            
            else:
                cv2.circle(self.rect_img, (x, y), 6, self.blue, 2)
                cv2.line(self.rect_img, (0, y), (x, y), self.blue, 3)
                cv2.line(self.rect_img, (x, 0), (x, y), self.blue, 3)
                self.point_toggle = False
                
                self.bX, self.bY = x, y
                self.minX, self.maxX = min(self.aX, self.bX), max(self.aX, self.bX)
                self.minY, self.maxY = min(self.aY, self.bY), max(self.aY, self.bY)
                
        