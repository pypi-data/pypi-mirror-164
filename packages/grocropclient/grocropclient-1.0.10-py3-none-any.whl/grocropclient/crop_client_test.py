from gro_crop_client import GroCropClient
crop_client = GroCropClient(api_host='api.gro-intelligence.com',
                            access_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjEyNTgxLCJob3N0VHlwZSI6ImFwaSIsImlhdCI6MTYyODE5MzU4OX0.rVZjlLSJbipiHmr2pqTliEY782sWEh8gGHJWTSufP8c')
print(crop_client.get_dtn_fertilizer_prices(fertilizer_id=4361, region_id=0))
