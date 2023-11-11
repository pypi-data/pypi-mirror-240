from pypscloud.pypscloud import *

def main():
    ps = PSCommon('prod')
    s3 = PSS3
    
    ps.login()
    ps_post_cmd(13817,7)

main()