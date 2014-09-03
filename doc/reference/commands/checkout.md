### checkout
The `checkout` command restores any image from the history. 

	# Checkout a old image by its id
    > spoon checkout 73dfe6973074 restored-image
    
    Restored the restored-image:head image
    
By default the new name has to be unique. The `--overwrite` flags allows to overwrite a existing image name.