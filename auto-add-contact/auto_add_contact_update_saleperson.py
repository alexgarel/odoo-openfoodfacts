# It's annoying to have rec ords created by a platform user without having sales persons set ! Set it.

# only if user is an internal user (share=False and @ in login)
is_internal_user = (not env.user.share) and ("@" in env.user.login)
if not record.user_id and is_internal_user:
  record.write({
    'user_id': env.user.id,
  })
