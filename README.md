# Generate Fluorescent Masks from Phase Cell Images


## Downloading Pix2Pix repo:
1. Git clone the [Pix2Pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) repo:
    ```
    git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
    cd pytorch-CycleGAN-and-pix2pix
    ```
2. Run the below command to install environment or follow installation instructions in the Pix2Pix repository.
   ```
    pip install -r requirements.txt
   ``` 

## Steps to generate the masks
1. Convert all *.tif* images to *.jpg* using batch process option in Imagej as python does not convert *.tif* to *.jpg* or *.png* with these images as some particular factor is misisng and we get plain white or plain black images
2. Create a folder with two subdirs A and B and then create a test dir in both of them copy the *.jpg* images to both of the test dirs. 
3. Ensure the name of the same image does not get changed and is maintained in the A and B folders
3. Run rename_images.py to rename and add a  suffix "_A" and "_B" to them. Update the path to folder A and B in lines 58-59 of rename_images.py
4. Then run the following command  in the pix2pix codebase to create testing data

    ```
    python datasets/combine_A_and_B.py  --fold_A <path_to_A> --fold_B <path_to_B> --fold_AB <path_to_parent_A> --use_AB 
    ```
5. Run the following command from pix2pix codebase to generate fluorescent images
    ```
      python test.py --dataroot <path_to_parent_A>  \
      --name phase_fluoro \
      --model pix2pix --direction AtoB \
      --checkpoints_dir <path_to_checkpoints> \
      --results_dir <path_to_poutput_dir> \
      --num_test=<num_of_images> --preprocess scale_width --load_size 1024
    ```

