# How_to_pass_dynamic_values_to_galaxy_bioinformatics

Tried a lot of different approaches to pass the username or user id to a galaxy tool configuration, nothing seemed to work,
e.g. the __user_id__ or user_name could not be passed to a function referenced by dynamic_options, e.g.:

<param name="mytool" type="select" dynamic_options="mystuff(userid=__user_id__)" />
 or
 <param name="mytool" type="select" dynamic_options="mystuff(username=__user_name__)" />
 
 did not work, neither other approaches such as username='$__user_name__' or ${__user_name__} or '${__user_name__}'
 
 it seems that the reserved variables from this document here cannot be accessed by a dynamic_options method:
 https://wiki.galaxyproject.org/Admin/Tools/ToolConfigSyntax?action=show&redirect=Admin%2FTools%2FTool+Config+Syntax#A.3Ccode.3E_tag_set
 
 The only solution or working approach is to submit the __trans__ dictionary, which is accessible in the referencing
 dynamics_option function.
 
 Because this feature is not well documented, here is some example code to get you started.
 
