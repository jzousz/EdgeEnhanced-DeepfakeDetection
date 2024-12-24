from util import mkdir


# root to the testsets
dataroot = '/data'
dataroot = '/scratch/project_2006362/zoujian/dataset/diffusion_model_deepfakes_lsun_bedroom/test'


# list of synthesis algorithms
print(dataroot)
# vals = ['progan', 'stylegan', 'biggan', 'cyclegan', 'stargan', 'gaugan',
#         'stylegan2', 'whichfaceisreal',
#         'ADM','Glide','Midjourney','stable_diffusion_v_1_4','stable_diffusion_v_1_5','VQDM','wukong','DALLE2']
vals = [  'ADM',  'DDPM' ,'IDDPM',  'LDM',  'PNDM', 'Diff-ProjectedGAN',  'Diff-StyleGAN2',    'ProGAN','ProjectedGAN','StyleGAN']

