# bids-error-examples

This repository contains a set of [BIDS](https://bids.neuroimaging.io/)**-incompatible** datasets which showcase BIDS errors.
This error case reference is chiefly useful for writing validator software tests.

**ALL RAW DATA FILES IN THIS REPOSITORY ARE EMPTY!**

However for some of the data, the headers containing the metadata are still
intact. (For example the NIfTI headers for `.nii` files, the BrainVision data
headers for `.vhdr` files, or the OME-XML headers for `.ome.tif` files.)

Headers are intact for the following datasets:

- `synthetic`
- Most EEG or iEEG data in BrainVision format (e.g., `eeg_matchingpennies`)

## Error Annotation

Errors are described in human-readable form under the `# BIDS Error` heading at the end of each dataset's `README` file.
