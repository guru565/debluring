import cv2
import numpy as np
import time

start_time = time.time()

irem = cv2.imread('py.jpg')          
irem_gray = cv2.cvtColor(irem, cv2.COLOR_BGR2GRAY)  
ozcan = irem_gray.astype(np.float64) / 255.0    
x, y = ozcan.shape
fft_irem = np.fft.fft2(ozcan, s=(x, y))
n = 2 * round(y / 100) + 1  
mask = np.ones((n, n), dtype=np.float64)
mask /= mask.sum()
mask_padded = np.zeros_like(ozcan)
mask_padded[:n, :n] = mask
mask_FFT = np.fft.fft2(mask_padded, s=(x, y))
Blur_FFT_Image = fft_irem * mask_FFT
Blur_Image = np.fft.ifft2(Blur_FFT_Image)
Blur_Image = np.abs(Blur_Image)
eps = 1e-8  
Deblurred = Blur_FFT_Image / (mask_FFT + eps)
Deblurred_ifft = np.real(np.fft.ifft2(Deblurred))

original_display = (ozcan * 255).astype(np.uint8)
blurred_display = np.clip(Blur_Image * 255, 0, 255).astype(np.uint8)
deblurred_display = np.clip(Deblurred_ifft * 255, 0, 255).astype(np.uint8)
cv2.imshow('Original Grayscale Image', original_display)
cv2.imshow('Blurred Image', blurred_display)
cv2.imshow('Deblurred Image', deblurred_display)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Execution Time: {:.2f} seconds".format(time.time() - start_time))
