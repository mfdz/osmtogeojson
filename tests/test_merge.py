from osmtogeojson import merge

def test_line_cleanup():
    expected_output = {"geometry": {"coordinates": [[-74.3398261, 40.7159394], [-74.3399473, 40.7158838], [-74.340076, 40.715781], [-74.340283, 40.715584], [-74.340515, 40.71532], [-74.340663, 40.715158], [-74.341017, 40.714769], [-74.341301, 40.714454], [-74.341526, 40.714204], [-74.341986, 40.713772], [-74.342247, 40.7135594], [-74.3426316, 40.7132707], [-74.342866, 40.713089], [-74.343733, 40.712494], [-74.344032, 40.712314], [-74.344484, 40.712095], [-74.3446858, 40.7120132], [-74.3448779, 40.7119443], [-74.3452756, 40.711861], [-74.3454053, 40.7118325], [-74.3459905, 40.7117366], [-74.3460798, 40.711726], [-74.3463025, 40.7116996], [-74.3466338, 40.7116869], [-74.3468979, 40.711696], [-74.3471043, 40.711716], [-74.3479281, 40.7118145], [-74.3489379, 40.7119528], [-74.3501015, 40.712103], [-74.350224, 40.7121066], [-74.3504232, 40.7120902], [-74.3505457, 40.7120629], [-74.3506729, 40.7120247], [-74.3507881, 40.711961], [-74.3513343, 40.7116021], [-74.3516964, 40.7113985], [-74.3517948, 40.7113515], [-74.3521998, 40.7111568], [-74.3527195, 40.7109302], [-74.3528203, 40.7108974], [-74.3529236, 40.7108738], [-74.3530367, 40.7108588], [-74.3531516, 40.7108537], [-74.3532713, 40.7108577], [-74.3533724, 40.710877], [-74.3534756, 40.7109085], [-74.354192, 40.7111772], [-74.3543027, 40.7112265], [-74.3543595, 40.7112596], [-74.354416, 40.7112926], [-74.3567618, 40.7126586], [-74.3572078, 40.7129082], [-74.3578675, 40.7133036], [-74.3579405, 40.7133473], [-74.3580134, 40.713389], [-74.3587118, 40.7137885], [-74.3587877, 40.7138325], [-74.3588624, 40.713872], [-74.3596921, 40.7143261], [-74.3599328, 40.7144575], [-74.3600412, 40.71453], [-74.3602565, 40.714664], [-74.3605969, 40.7148482], [-74.3606745, 40.7148928], [-74.360883, 40.715014], [-74.361109, 40.715147], [-74.3617045, 40.7155075], [-74.361756, 40.7155387], [-74.3618895, 40.7156195], [-74.3625049, 40.715992], [-74.3627406, 40.7161347], [-74.3628462, 40.7161948], [-74.3630028, 40.7162819], [-74.3635144, 40.7165666], [-74.3638801, 40.7167633], [-74.3639786, 40.7168147], [-74.3640552, 40.7168705], [-74.3640812, 40.7168963], [-74.3641248, 40.7169486], [-74.3641998, 40.7170601], [-74.3645555, 40.7176226], [-74.3647043, 40.7178627], [-74.364882, 40.7180483], [-74.3652037, 40.7183724], [-74.3653045, 40.7184632], [-74.3655513, 40.7187133], [-74.3656857, 40.7188749], [-74.3657466, 40.7189822], [-74.3663557, 40.7202097], [-74.3664162, 40.720327], [-74.3664535, 40.7203992], [-74.3666395, 40.7207598], [-74.3668291, 40.7211092], [-74.367043, 40.721459], [-74.367153, 40.72166], [-74.3672527, 40.7218481], [-74.3673796, 40.7220233], [-74.3674811, 40.7221579], [-74.3675812, 40.7222829], [-74.3678236, 40.7225392], [-74.3680497, 40.7227483], [-74.3682514, 40.7229047], [-74.3684626, 40.7230576], [-74.3687747, 40.7232504], [-74.3690046, 40.7233935], [-74.3699846, 40.7239963], [-74.3707351, 40.7244842], [-74.3717088, 40.725165], [-74.3718578, 40.7252758], [-74.3723894, 40.7256267], [-74.3732517, 40.7261693], [-74.3742457, 40.7267334], [-74.3743468, 40.7267949], [-74.3744468, 40.7268677], [-74.3745205, 40.7269253], [-74.3746071, 40.7270153], [-74.3750385, 40.7274969], [-74.3754127, 40.7279106], [-74.375602, 40.7281198], [-74.3759428, 40.7285217], [-74.3762213, 40.7288502], [-74.3764074, 40.7290502], [-74.3767688, 40.7294124]], "type": "LineString"}, "id": "relation/563476", "properties": {"id": "relation/563476", "network": "US:NJ:Union", "ref": "651", "route": "road", "type": "route"}, "type": "Feature"}

    dirty_input = {"type": "Feature", "id": "relation/563476", "properties": {"network": "US:NJ:Union", "ref": "651", "route": "road", "type": "route", "id": "relation/563476"}, "geometry": {"type": "MultiLineString", "coordinates": [[[-74.3398261, 40.7159394], [-74.3399473, 40.7158838], [-74.340076, 40.715781], [-74.340283, 40.715584], [-74.340515, 40.71532], [-74.340663, 40.715158], [-74.341017, 40.714769], [-74.341301, 40.714454], [-74.341526, 40.714204], [-74.341986, 40.713772], [-74.342247, 40.7135594]], [[-74.342247, 40.7135594], [-74.3426316, 40.7132707], [-74.342866, 40.713089], [-74.343733, 40.712494], [-74.344032, 40.712314], [-74.344484, 40.712095], [-74.3446858, 40.7120132], [-74.3448779, 40.7119443]], [[-74.3448779, 40.7119443], [-74.3452756, 40.711861], [-74.3454053, 40.7118325], [-74.3459905, 40.7117366], [-74.3460798, 40.711726], [-74.3463025, 40.7116996], [-74.3466338, 40.7116869], [-74.3468979, 40.711696], [-74.3471043, 40.711716], [-74.3479281, 40.7118145], [-74.3489379, 40.7119528], [-74.3501015, 40.712103], [-74.350224, 40.7121066], [-74.3504232, 40.7120902], [-74.3505457, 40.7120629], [-74.3506729, 40.7120247], [-74.3507881, 40.711961], [-74.3513343, 40.7116021]], [[-74.3513343, 40.7116021], [-74.3516964, 40.7113985]], [[-74.3516964, 40.7113985], [-74.3517948, 40.7113515]], [[-74.3517948, 40.7113515], [-74.3521998, 40.7111568]], [[-74.3521998, 40.7111568], [-74.3527195, 40.7109302], [-74.3528203, 40.7108974], [-74.3529236, 40.7108738], [-74.3530367, 40.7108588], [-74.3531516, 40.7108537], [-74.3532713, 40.7108577], [-74.3533724, 40.710877], [-74.3534756, 40.7109085], [-74.354192, 40.7111772], [-74.3543027, 40.7112265], [-74.3543595, 40.7112596], [-74.354416, 40.7112926], [-74.3567618, 40.7126586], [-74.3572078, 40.7129082], [-74.3578675, 40.7133036], [-74.3579405, 40.7133473], [-74.3580134, 40.713389], [-74.3587118, 40.7137885], [-74.3587877, 40.7138325], [-74.3588624, 40.713872], [-74.3596921, 40.7143261], [-74.3599328, 40.7144575], [-74.3600412, 40.71453], [-74.3602565, 40.714664], [-74.3605969, 40.7148482], [-74.3606745, 40.7148928], [-74.360883, 40.715014]], [[-74.360883, 40.715014], [-74.361109, 40.715147], [-74.3617045, 40.7155075], [-74.361756, 40.7155387], [-74.3618895, 40.7156195], [-74.3625049, 40.715992], [-74.3627406, 40.7161347]], [[-74.3639786, 40.7168147], [-74.3640552, 40.7168705], [-74.3640812, 40.7168963], [-74.3641248, 40.7169486], [-74.3641998, 40.7170601], [-74.3645555, 40.7176226], [-74.3647043, 40.7178627], [-74.364882, 40.7180483]], [[-74.3635144, 40.7165666], [-74.3638801, 40.7167633], [-74.3639786, 40.7168147]], [[-74.3627406, 40.7161347], [-74.3628462, 40.7161948], [-74.3630028, 40.7162819], [-74.3635144, 40.7165666]], [[-74.364882, 40.7180483], [-74.3652037, 40.7183724]], [[-74.3652037, 40.7183724], [-74.3653045, 40.7184632], [-74.3655513, 40.7187133], [-74.3656857, 40.7188749], [-74.3657466, 40.7189822], [-74.3663557, 40.7202097], [-74.3664162, 40.720327], [-74.3664535, 40.7203992], [-74.3666395, 40.7207598], [-74.3668291, 40.7211092], [-74.367043, 40.721459], [-74.367153, 40.72166], [-74.3672527, 40.7218481], [-74.3673796, 40.7220233], [-74.3674811, 40.7221579], [-74.3675812, 40.7222829], [-74.3678236, 40.7225392], [-74.3680497, 40.7227483], [-74.3682514, 40.7229047], [-74.3684626, 40.7230576], [-74.3687747, 40.7232504], [-74.3690046, 40.7233935], [-74.3699846, 40.7239963], [-74.3707351, 40.7244842], [-74.3717088, 40.725165], [-74.3718578, 40.7252758], [-74.3723894, 40.7256267], [-74.3732517, 40.7261693], [-74.3742457, 40.7267334], [-74.3743468, 40.7267949], [-74.3744468, 40.7268677], [-74.3745205, 40.7269253], [-74.3746071, 40.7270153], [-74.3750385, 40.7274969], [-74.3754127, 40.7279106], [-74.375602, 40.7281198], [-74.3759428, 40.7285217], [-74.3762213, 40.7288502], [-74.3764074, 40.7290502]], [[-74.3767688, 40.7294124], [-74.3764074, 40.7290502]]]}}

    assert merge.merge_line_string(dirty_input) == expected_output
