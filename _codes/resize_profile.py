import sanghyunjo as shjo

image = shjo.imread('./assets/img/profile.jpg')

ih, iw = image.shape[:2]
print((iw, ih))

crop_ih = int(ih * 0.7)
crop_image = image[:crop_ih, :]

# shjo.imshow('Demo', crop_image, wait=0)

crop_image = shjo.resize(crop_image, scale=0.7) # 
shjo.imwrite('./assets/img/profile_cropped.jpg', crop_image)