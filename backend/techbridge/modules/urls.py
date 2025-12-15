from django.urls import path
from .views import (
    GenerateModuleAPI,
    ModuleDetailAPI,
    ModuleTestDetailAPI,
    SubmitModuleTestAPI,
    RegenerateTestAPI
)

urlpatterns = [
    path("generate/", GenerateModuleAPI.as_view()),
    path("<int:module_id>/", ModuleDetailAPI.as_view()),
    path("<int:module_id>/test/", ModuleTestDetailAPI.as_view()),
    path("<int:module_id>/test/submit/", SubmitModuleTestAPI.as_view()),
    path("<int:module_id>/test/regenerate/", RegenerateTestAPI.as_view()),
]
