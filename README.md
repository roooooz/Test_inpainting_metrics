# Test_inpainting_metrics

The steps of test the inpainting metrics of irregular holes.

The Irregular Mask Dataset used for test can be download publically from the [website](https://nv-adlr.github.io/publication/partialconv-inpainting).

The test procedure is referred to [edge-connect](https://arxiv.org/abs/1901.00212), in which we divide the mask set into several groups according to the relative masked area ratio: 0~10%, 10%~20%, 20%~30%, 30%~40%, 40%~50%, 50%~60%. Since the provided testset contains 12,000 mask images totally, each groups only contain 2,000 images. For test experiment, we will randomly select 10,000 test images as the testset. To make the number of each groups consistent to the number of testset, we extend the number of each mask groups to 10,000 by duplicating 5 times.

### The details of the test procedure:

1. Classify the Irregular Mask Dataset to several groups: 0~10%, 10%~20%, 20%~30%, 30%~40%, 40%~50%， 50%~60%.

2. Extend the number of each mask groups to 10,000 by duplicating 5 times.

3. Randomly select 10,000 test images as the testset.

4. Mask the testset using each mask groups, generate corresponding masked image groups.

6. Use the inpainting method complete the masked images in each masked image groups, generate each inpainted image groups.

5. Test the inpainting metrics for each inpainted image groups.

### The function of each file:

- **classify_mask.py**: classify the Irregular Mask Dataset to several groups, each groups contains 2,000 mask images, output each groups file list. After that, we need duplicate the file list 5 times manually.

- **gen_mask.py**: generate the corresponding mask according to the mask flie list generated in last step.

- **mask_image.py**: generate the masked test images, using 10,000 test images and 10,000 mask images.

- **random_pick.py**: random select 10,000 images.


### Evaluating
To evaluate the model, we use a modified **metrics.py** [from here](https://github.com/knazeri/edge-connect) to evaluate the model using PSNR, SSIM and Mean Absolute Error:

```bash
python metrics.py --data-path [path to validation set] --output-path [path to model output]
```

To measure the Fréchet Inception Distance (FID score), run **fid_score.py** [from here](https://github.com/mseitzer/pytorch-fid) which uses the pretrained weights from PyTorch's Inception model.

```bash
python fid_score.py --path [path to validation, path to model output] --gpu [GPU id to use]
```


Moreover this procedure, we can also directly process the image to masked image when testing. We prepare 10,000 test images and 2,000 mask images for each groups. And then, for each input test image, we random select a mask to mask this test image and inpaint it. By this way, it can leave out some tedious steps.
