print('Let\'s start with basic properties:')
import mea_med_mod_sd
x=int(input('Enter any percentile u want to find: '))
print('''
25%: {:.3f}
50%: {:.3f}
75%: {:.3f}
{}%: {:.3f}
'''.format(mea_med_mod_sd.percentile(mea_med_mod_sd.lst,25),
mea_med_mod_sd.percentile(mea_med_mod_sd.lst,50),
mea_med_mod_sd.percentile(mea_med_mod_sd.lst,75),
x,
mea_med_mod_sd.percentile(mea_med_mod_sd.lst,x)
))
