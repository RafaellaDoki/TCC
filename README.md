# Dataset tools
## How to use the dataset tools
### Get branch
First download this repository branch, by clonning and switch to this branch:

<pre><code>git clone git@github.com:RafaellaDoki/TCC.git
git checkout dataset_tools
</code></pre>

Or by fetching the lasted data from existent repository:

<pre><code>git pull
git checkout dataset_tools
</code></pre>
### Put files in right location
Next you need to extract the jpg images from no tumor dataset to the "*no*" folder.

### Run the script
Finaly just run the "*convert_img_to_mat.sh*" to generate the final *mat* files in the "*no_mat*" folder

<pre><code>./convert_img_to_mat.sh
</code></pre>
