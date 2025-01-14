from django.contrib import admin
from dbadmin.models import Course, Outcome, Reviewer, Institution


# list_display = what we want shown in the admin site
# search_fields = what we want to search by, seems to do all at once
class CourseAdmin(admin.ModelAdmin):
    list_display = ("CourseNumber", "CourseName", "CourseDescription", "CourseCredit",
                    "CourseEquivalenceNonOC", "InstitutionID", "ReviewerID")
    search_fields = ("CourseNumber",)


class OutcomeAdmin(admin.ModelAdmin):
    list_display = ("CourseNumber", "OutcomeDescription")
    search_fields = ("CourseNumber",)


class ReviewerAdmin(admin.ModelAdmin):
    list_display = ("ReviewerName", "ReviewerPhone", "ReviewerEmail", "ReviewerDepartment")
    search_fields = ("ReviewerName",)


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("InstitutionName", "InstitutionAddress", "InstitutionCity", "InstitutionState",
                    "InstitutionZipcode", "InstitutionWebSite")
    search_fields = ("InstitutionName",)


# admin_site = MyAdminSite()
admin.site.register(Course, CourseAdmin)
admin.site.register(Outcome, OutcomeAdmin)
admin.site.register(Reviewer, ReviewerAdmin)
admin.site.register(Institution, InstitutionAdmin)


# Register your models here.
