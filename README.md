Images are nowadays an integral part of our lives, whether in scientific applications or social networking and where there is an image, the concept of blurring might occur. Blurring is a major cause of image degradation and decreases the quality of an image. Blur occur due to the atmospheric commotion as well as the improper setting of a camera. Along with blur effects, noise also corrupts the captured image. Deblurring is the process of removing blurs and restoring the high-quality latent image. Blur can be various types like Motion blur, Gaussian blur, Average blur, Defocus blur etc. There are many methods present in literature, and we examine different methods and technologies with their advantages and disadvantages.
The technique used in the provided deblurring.py script is Wiener filtering in the frequency domain for image deblurring. Here's a breakdown:

Key Steps:
Grayscale Conversion: The input image is converted to grayscale.

Fourier Transform: The grayscale image is transformed to the frequency domain using np.fft.fft2.

Blurring Kernel Creation: A uniform averaging filter (a normalized box filter) is created and padded to the image size.

Blurring Process:

The image is blurred in the frequency domain by multiplying its FFT with the FFT of the blur mask.

Inverse FFT is applied to get the blurred image.

Deblurring Process:

The blurred image's FFT is divided by the blur kernel's FFT (with a small epsilon added to avoid division by zero).

This effectively reverses the blurring, assuming no noise.
