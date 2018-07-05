"""
"""
#%% Libraries

import itk
import read_image as ri
#%% Inputs

filename_net_output = "/Users/pzandiyeh/Desktop/banafshehs_data/net_result.nii"
filename_grnd_truth = "/Users/pzandiyeh/Desktop/banafshehs_data/grndth.nii"
verbose = False

#%% Reading the inputs
net_output_image = itk.imread(filename_net_output) # Network output
grnd_truth_image = itk.imread(filename_grnd_truth) # Ground truth image

if verbose:
    print(net_output_image)
    print(grnd_truth_image)
#%% Modifying the type of pixel 
CastImageFilterType = itk.CastImageFilter[ri.get_itk_image_type(filename_net_output),itk.Image[itk.ctype("short"),3]]
castFilter1 = CastImageFilterType.New()

if verbose:
    print castFilter1

castFilter1.SetInput(net_output_image)
castFilter1.Update()
net_output_image_modified = castFilter1.GetOutput()
if verbose:
    print("network output image (type modified)")

castFilter2 = CastImageFilterType.New()
castFilter2.SetInput(grnd_truth_image)
castFilter2.Update()
grnd_truth_image_modified = castFilter2.GetOutput()

if verbose:
    print("ground trutch image (type modified)")
    print(grnd_truth_image_modified)
    
#%% 
itk.imwrite(grnd_truth_image_modified,"/Users/pzandiyeh/Desktop/banafshehs_data/grnd_truth_image_modified.nii")
itk.imwrite(net_output_image_modified,"/Users/pzandiyeh/Desktop/banafshehs_data/net_output_image_modified.nii")


#%%
ImageType = itk.Image[itk.ctype("short"),3]

FilterType = itk.HausdorffDistanceImageFilter[ImageType,ImageType]

filter = FilterType.New()
filter.SetInput1(grnd_truth_image_modified)
filter.SetInput2(net_output_image_modified)

filter.Update()

print(filter.GetHausdorffDistance())        # Gets the distance
print(filter.GetAverageHausdorffDistance()) # Get the average Hausdroff Distance

if verbose:
    print(filter)

