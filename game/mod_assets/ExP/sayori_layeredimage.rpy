
layeredimage sayori base: 
    at Flatten
    # at AutofocusDisplayable(name="sayori") # if you used autofocus
    always paths.sayori("bases", "base", "face") #Always need this face.


    # Autofocus function on changing the color of characters depending on the time of day.
    # group autofocus_coloring:
    #     attribute day default null
    #     attribute dawn null
    #     attribute sunset null
    #     attribute night null
    #     attribute evening null

    group outfit:
        attribute uniform default null
        attribute casual null
    
    # (Formerly Blush) Cheek Expressions
    group cheek: 
        attribute norm default null # Normal
        attribute eh null # Awkward/Eh.
        attribute shy null # Blushing (shy used as synomyn)
        attribute shyeh null # Both Shy and Awkward
    
    #Left arm variants
    group left if_any(["uniform"]):
        attribute ldown default:
            paths.sayori("bases", "base", "uniform_left_down")
        attribute lup:
            paths.sayori("bases", "base", "uniform_left_up")
    
    group left if_any(["casual"]):
        attribute ldown default:
            paths.sayori("bases", "base", "casual_left_down")
        attribute lup:
            paths.sayori("bases", "base", "casual_left_up")
    
    
    
    #Right arm variants
    group right if_any(["uniform"]):
        attribute rdown default:
            paths.sayori("bases", "base", "uniform_right_down")
        attribute rup:
            paths.sayori("bases", "base", "uniform_right_up")
    
    group right if_any(["casual"]):
        attribute rdown default:
            paths.sayori("bases", "base", "casual_right_down")
        attribute rup:
            paths.sayori("bases", "base", "casual_right_up")
    
    # Nose
    group nose:
        attribute nose default if_any(["norm"]): # default nose
            paths.sayori("nose", "base", "nose1")
        attribute nose default if_any(["eh"]): # default nose when "awkward"
            paths.sayori("nose", "base", "nose2")
        attribute nose default if_any(["shy"]): # default nose when "blushing"
            paths.sayori("nose", "base", "nose3")
        attribute nose default if_any(["shyeh"]): # default nose when "blushing and awkward"
            paths.sayori("nose", "base", "nose4")
        
        attribute nose1:
            paths.sayori("nose", "base", "nose1")
        attribute nose2:
            paths.sayori("nose", "base", "nose2")
        attribute nose3:
            paths.sayori("nose", "base", "nose3")
        attribute nose4:
            paths.sayori("nose", "base", "nose4")
        attribute nose5:
            paths.sayori("nose", "base", "nose5")

    # Mouth
    group mouth:
        attribute mouth_a:
            paths.sayori("mouth", "base", "mouth_a")
        attribute mouth_b:
            paths.sayori("mouth", "base", "mouth_b")
        attribute mouth_c:
            paths.sayori("mouth", "base", "mouth_c")
        attribute mouth_d:
            paths.sayori("mouth", "base", "mouth_d")
        attribute mouth_e:
            paths.sayori("mouth", "base", "mouth_e")
        attribute mouth_f:
            paths.sayori("mouth", "base", "mouth_f")
        attribute mouth_g:
            paths.sayori("mouth", "base", "mouth_g")
        attribute mouth_h:
            paths.sayori("mouth", "base", "mouth_h")
        attribute mouth_i:
            paths.sayori("mouth", "base", "mouth_i")
        attribute mouth_j:
            paths.sayori("mouth", "base", "mouth_j")
        attribute mouth_k:
            spaths.sayori("mouth", "base", "mouth_k")
        attribute mouth_l:
            paths.sayori("mouth", "base", "mouth_l")
        attribute mouth_:
            paths.sayori("mouth", "base", "mouth_m")
        attribute mouth_n:
            paths.sayori("mouth", "base", "mouth_n")
        attribute mouth_o:
            paths.sayori("mouth", "base", "mouth_o")
        attribute mouth_p:
            paths.sayori("mouth", "base", "mouth_p")
        attribute mouth_q:
            paths.sayori("mouth", "base", "mouth_q")
        attribute mouth_r:
            paths.sayori("mouth", "base", "mouth_r")
    
    # Eyes
    group eyes:
        attribute eyes_a:
            paths.sayori("eyes", "base", "eyes_a")
        attribute eyes_b:
            paths.sayori("eyes", "base", "eyes_b")
        attribute eyes_c:
            paths.sayori("eyes", "base", "eyes_c")
        attribute eyes_d:
            paths.sayori("eyes", "base", "eyes_d")
        attribute eyes_e:
            paths.sayori("eyes", "base", "eyes_e")
        attribute eyes_f:
            paths.sayori("eyes", "base", "eyes_f")
        attribute eyes_g:
            paths.sayori("eyes", "base", "eyes_g")
        attribute eyes_h:
            paths.sayori("eyes", "base", "eyes_h")
        attribute eyes_i:
            paths.sayori("eyes", "base", "eyes_i")
        attribute eyes_j:
            paths.sayori("eyes", "base", "eyes_j")
        attribute eyes_k:
            paths.sayori("eyes", "base", "eyes_k")
        attribute eyes_l:
            paths.sayori("eyes", "base", "eyes_l")
        attribute eyes_m:
            paths.sayori("eyes", "base", "eyes_m")
        attribute eyes_n:
            paths.sayori("eyes", "base", "eyes_n")
        attribute eyes_o:
            paths.sayori("eyes", "base", "eyes_o")
        attribute eyes_p:
            paths.sayori("eyes", "base", "eyes_p")
        attribute eyes_q:
            paths.sayori("eyes", "base", "eyes_q")
        attribute eyes_r:
            paths.sayori("eyes", "base", "eyes_r")
        attribute eyes_s:
            paths.sayori("eyes", "base", "eyes_s")
        attribute eyes_t:
            paths.sayori("eyes", "base", "eyes_t")
        attribute eyes_u:
            paths.sayori("eyes", "base", "eyes_u")
    
    group eyebrows:
        ### Default Eyebrows
        attribute brow default if_any(["fine", "happy", "lightly_amazed", "flustered", "shocked", "neut","happ","lsur","flus","shoc"]):
            paths.sayori("brows", "base", "b1a")
        attribute brow default if_any(["crying", "panicked", "yandere", "tense", "sad","cry","pani","yand","nerv"]):
            paths.sayori("brows", "base", "b1b")
        attribute brow default if_any(["laughing", "very_amazed", "unease", "alluring", "laug","vsur","worr","sedu"]):
            paths.sayori("brows", "base", "b1c")
        attribute brow default if_any(["annoyed", "anno","pout"]):
            paths.sayori("brows", "base", "b1d")
        attribute brow default if_any(["angry", "angr","vang"]):
            paths.sayori("brows", "base", "b1e")
        attribute brow default if_any(["curious", "doubtful", "curi","doub"]):
            paths.sayori("brows", "base", "b1f")
        
        ### The following brows are for moods that differ between open and closed eyes:
        attribute brow default if_any(["aloof", "dist"]) if_all(["open_eyes"]) if_not(["closed_eyes", "ce"]):
            paths.sayori("brows", "base", "b2a")
        attribute brow default if_any(["aloof", "dist"]) if_all(["closed_eyes"]) if_not(["open_eyes", "oe"]):
            paths.sayori("brows", "base", "b3c")
        
        attribute brow default if_any(["aloof", "dist"]) if_all(["oe"]) if_not(["closed_eyes", "ce"]):
            paths.sayori("brows", "base", "b2a")
        attribute brow default if_any(["aloof", "dist"]) if_all(["ce"]) if_not(["open_eyes", "oe"]):
            paths.sayori("brows", "base", "b3c")
        
    # Eyebrows
    group eyebrows:
        attribute brow_a:
            paths.sayori("brows", "base", "eyebrows_a")
        attribute brow_b:
            paths.sayori("brows", "base", "eyebrows_b")
        attribute brow_c:
            paths.sayori("brows", "base", "eyebrows_c")
        attribute brow_d:
            paths.sayori("brows", "base", "eyebrows_d")
        attribute brow_e:
            paths.sayori("brows", "base", "eyebrows_e")
        attribute brow_f:
            paths.sayori("brows", "base", "eyebrows_f")
        attribute brow_g:
            paths.sayori("brows", "base", "eyebrows_g")
        attribute brow_h:
            paths.sayori("brows", "base", "eyebrows_h")
        attribute brow_i:
            paths.sayori("brows", "base", "eyebrows_i")
        attribute brow_j if_any(["eyes_o","eyes_p","eyes_q","eyes_r","eyes_s"]):
            paths.sayori("brows", "base", "eyebrows_j")
        attribute brow_k if_any(["eyes_o","eyes_p","eyes_q","eyes_r","eyes_s"]):
            paths.sayori("brows", "base", "eyebrows_k")
        attribute brow_l if_any(["eyes_o","eyes_p","eyes_q","eyes_r","eyes_s"]):
            paths.sayori("brows", "base", "eyebrows_l")
    
    #This group is intentionally last on this list, so it will render over top 
    # of every other thing on the face.
    group special:
        attribute s_scream:
            paths.sayori("bases", "base", "special_scream")


    ## For use if NBE assets is installed
    # group blink:
    #     attribute blink_a default if_not(["eyes_o", "eyes_p", "eyes_q", "eyes_r", "eyes_s", "eyes_t", "eyes_e", "eyes_f"]):
    #         ConditionSwitch("persistent.enable_nbe", "_say_blink_a", True, "sprite_blank")
    #     attribute no_blink:
    #         "sprite_blank"

layeredimage sayori tap: 
    at Flatten

    always paths.sayori("bases", "tapping", "face")

    group outfit:
        attribute uniform default null
        attribute casual null

    group cheek:
        attribute norm default null # Normal
        attribute eh null # Awkward/Eh.
        attribute shy null # Blushing (shy used as synomyn)
        attribute shyeh null # Both Shy and Awkward
        attribute vshy null # full face blush.
    
    group body:
        attribute uniform default if_any(["uniform"]):
            paths.sayori("bases", "tapping", "uniform_body")
        attribute casual default if_any(["casual"]):
            paths.sayori("bases", "tapping", "casual_body")

    group nose:
        attribute nose default if_any(["norm"]): #default nose
            paths.sayori("nose", "tapping", "nose1")
        attribute nose default if_any(["eh"]): #default nose when "awkward"
            paths.sayori("nose", "tapping", "noce2")
        attribute nose default if_any(["shy"]): #default nose when "blushing"
            paths.sayori("nose", "tapping", "nose3")
        attribute nose default if_any(["shyeh"]): #default nose when both "blushing" and "awkward"
            paths.sayori("nose", "tapping", "nose4")
        attribute nose default if_any(["vshy"]): #full face blush, obscures eyes/eyebrows.
            paths.sayori("nose", "tapping", "nose5")

        attribute nose1:
            paths.sayori("nose", "tapping", "nose1")
        attribute nose2:
            paths.sayori("nose", "tapping", "nose2")
        attribute nose3:
            paths.sayori("nose", "tapping", "nose3")
        attribute nose4:
            paths.sayori("nose", "tapping", "nose4")
        attribute nose5:
            paths.sayori("nose", "tapping", "nose5")
    
    group mouth:
        attribute mouth_a:
            paths.sayori("mouth", "tapping", "mouth_a")
        attribute mouth_b:
            paths.sayori("mouth", "tapping", "mouth_b")
        attribute mouth_c:
            paths.sayori("mouth", "tapping", "mouth_c")
        attribute mouth_d:
            paths.sayori("mouth", "tapping", "mouth_d")
    
    group eyes if_not(["nose5", "vshy"]): #Cannot show if full-face blush is present.
        attribute eyes_a:
            paths.sayori("eyes", "tapping", "eyes_a")
        attribute eyes_b:
            paths.sayori("eyes", "tapping", "eyes_b")
        attribute eyes_c:
            paths.sayori("eyes", "tapping", "eyes_c")
        attribute eyes_d:
            paths.sayori("eyes", "tapping", "eyes_d")
        attribute eyes_e:
            paths.sayori("eyes", "tapping", "eyes_e")
        attribute eyes_f:
            paths.sayori("eyes", "tapping", "eyes_f")
    
    group eyebrows if_not(["nose5", "vshy"]): #Cannot show if full-face blush is present.
        attribute brow_a:
            paths.sayori("brows", "tapping", "eyebrows_a")
        attribute brow_b:
            paths.sayori("brows", "tapping", "eyebrows_b.")

        attribute brow_c:
            paths.sayori("brows", "tapping", "eyebrows_c")
    
    ## For use if NBE assets is installed
    # group blink:
    #     attribute blink_a default if_not(["eyes_d", "eyes_e", "nose5", "vshy"]):
    #         ConditionSwitch("persistent.enable_nbe", "_say_blink_t_a", True, "sprite_blank")
    #     attribute no_blink:
    #         "sprite_blank"
