# HairCoSys Mobile Hair Segmentation 

## Hair Coloring 
This repo serves as a proof of concept of doing head segmentation. 

For hair coloring, MediaPipe can serve as the best solution. However using proofed hair segmentation, 

I have done training and weights for the model can be found on /checkpoints_haircoloring/best.pth

to do evaluation, you can use this command

> python main.py --test --data_path=dataset_haircoloring

## Top head detection and segmentation 

### dataset
dataset can be retrieved on Users/ferdy/Documents/project2/baseline/mobile.. 


Using the same model architecture, we can segment the top head from the background. 

to do prediction on single image, use this command 

> python predict.py -i=dataset_tophead/images/396.jpg -o=result/0.jpg --model_path=checkpoints/best.pth

Explanation on predict.py 
1. firstly it will calculate the hair loss area. 
2. after several founding, even for people with severely bald head, the hair loss ratio will not reach > 70%. 
3. we can use this as an indicator for people with white hair, based on observation, most ppl with white hair will have hair loss ratio around 80  ~ 90%
4. Therefore we adjust the contrast of the image by doing gamma correction, if the user has white hair, we try to increase the contrast between the scalp and the hair 
5. as a result, we could calculate a reasonable amount of hair loss ratio on white people.

![white hair calculation](/white_hair_calc.png "White hair result")

