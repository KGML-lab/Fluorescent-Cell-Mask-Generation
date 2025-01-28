import os

def rename_images(directory, suffix):
    for subdir in ['test', 'train']:
        path = os.path.join(directory, subdir)
        for filename in os.listdir(path):
            if filename.endswith('.jpg'):
                new_name = filename.replace(".jpg", "_{}.jpg".format(suffix))
                os.rename(os.path.join(path, filename), os.path.join(path, new_name))
import re

def rename_images_2(directory, suffix):
    for subdir in ['test', 'train']:
        path = os.path.join(directory, subdir)
        if os.path.exists(path):
            for filename in os.listdir(path):
                if filename.endswith('.jpg'):
                    # Define the desired suffix pattern
                    target_suffix = f"_{suffix}.jpg"
                    
                    # Check if the filename already has any suffix pattern (_suffix) before .jpg
                    match = re.search(r"_(\w+)\.jpg$", filename)
                    
                    if match:
                        current_suffix = match.group(1)
                        # If the current suffix is the target suffix, skip renaming
                        if current_suffix == suffix:
                            continue
                        # Otherwise, replace the current suffix with the desired suffix
                        new_name = re.sub(r"_(\w+)\.jpg$", target_suffix, filename)
                    else:
                        # No suffix present; add the desired suffix
                        new_name = filename.replace(".jpg", target_suffix)
                    
                    # Rename the file
                    os.rename(os.path.join(path, filename), os.path.join(path, new_name))
                    print(f"Renamed {filename} to {new_name}")


# funtion to match filenames in phase and fluro dircetories. phase has 2t and fluoro has 1 t, so matching them
def replace_2t_with_1t(directory):
    """Rename files replacing '1t' with '2t' in their filenames."""
    for subdir in ['test', 'train']:
        path = os.path.join(directory, subdir)
        for filename in os.listdir(path):
            if '2t' in filename and filename.endswith('.jpg'):
                # Replace '2t' with '1t' in the filename
                new_name = filename.replace('2t', '1t')
                os.rename(os.path.join(path, filename), os.path.join(path, new_name))
# Rename images in directory A with _A suffix
#rename_images('./phase_to_cell_fluoro/A', 'A')

# Rename images in directory B with _B suffix
#rename_images('./phase_to_cell_fluoro/B', 'B')

#replace_2t_with_1t('./phase_to_cell_fluoro/A')

rename_images_2('./inference/B', 'B')
rename_images_2('./inference/A', 'A')

