from typing import Set, Tuple

try:
    from NEMO.models import Discipline as ProjectDiscipline
except:
    from NEMO.models import ProjectDiscipline


from NEMO.models import Account, AccountType, Project, User
from django.db.models import Q
from django.shortcuts import render
from django.views.decorators.http import require_GET

from NEMO_reports.decorators import accounting_or_manager_required
from NEMO_reports.views.reporting import (
    ACTIVITIES_PARAMETER_LIST,
    DEFAULT_PARAMETER_LIST,
    DataDisplayTable,
    ReportingParameters,
    SummaryDisplayTable,
    area_access,
    billing_installed,
    consumable_withdraws,
    custom_charges,
    get_core_facility,
    get_institution_type,
    get_institution,
    get_month_range,
    get_monthly_rule,
    get_rate_category,
    missed_reservations,
    report_export,
    reporting_dictionary,
    staff_charges,
    training_sessions,
    usage_events,
)


@accounting_or_manager_required
@require_GET
def unique_users(request):
    return unique_user_combination(request)


@accounting_or_manager_required
@require_GET
def unique_user_and_project_combinations(request):
    return unique_user_combination(request, "project_id")


@accounting_or_manager_required
@require_GET
def unique_user_and_account_combinations(request):
    return unique_user_combination(request, "project__account_id")


def unique_user_combination(request, combination=None):
    param_names = DEFAULT_PARAMETER_LIST + ACTIVITIES_PARAMETER_LIST
    params = ReportingParameters(request, param_names)
    start, end = params.start, params.end
    split_by_month = params.get_bool("split_by_month")
    cumulative_count = params.get_bool("cumulative_count")
    monthly_start = None
    if cumulative_count:
        split_by_month = True
        monthly_start, monthly_end = get_month_range(start)

    RateCategory = get_rate_category()
    CoreFacility = get_core_facility()
    InstitutionType = get_institution_type()
    Institution = get_institution()

    data = DataDisplayTable()
    if params.get_bool("detailed_data"):
        data.headers = [
            ("first", "First name"),
            ("last", "Last name"),
            ("username", "Username"),
            ("email", "Email"),
            ("active", "Active"),
            ("access_expiration", "Access expiration"),
        ]

        if combination == "project_id":
            data.add_header(("project", "Project"))
            data.add_header(("account", "Account"))
            if ProjectDiscipline.objects.exists():
                data.add_header(("discipline", "Discipline"))
            if AccountType.objects.exists():
                data.add_header(("account_type", "Account type"))
            if RateCategory and RateCategory.objects.exists():
                data.add_header(("rate_category", "Rate category"))
            if Institution and Institution.objects.exists():
                data.add_header(("institution_name", "Institution Name"))
                data.add_header(("institution_type", "Institution Type"))
            data.add_header(("combination_active", "Active"))
        elif combination:
            data.add_header(("account", "Account"))
            if AccountType.objects.exists():
                data.add_header(("account_type", "Account type"))
            data.add_header(("combination_active", "Active"))

        total_data_set = get_unique_user_combinations(params, start, end, combination)
        for user_combination in total_data_set:
            user = User.objects.get(pk=user_combination[0])
            data_row = {
                "first": user.first_name,
                "last": user.last_name,
                "username": user.username,
                "email": user.email,
                "active": user.is_active,
                "access_expiration": user.access_expiration,
            }
            if len(user_combination) >= 2 and user_combination[1]:
                if combination == "project_id":
                    project: Project = Project.objects.get(pk=user_combination[1])
                    data_row["project"] = project.name
                    data_row["account"] = project.account.name
                    data_row["discipline"] = project.discipline.name if project.discipline else ""
                    data_row["account_type"] = project.account.type.name if project.account.type else ""
                    if RateCategory and RateCategory.objects.exists():
                        data_row["rate_category"] = (
                            project.projectbillingdetails.category.name
                            if hasattr(project, "projectbillingdetails") and project.projectbillingdetails.category
                            else ""
                        )
                    if Institution and Institution.objects.exists():
                        data_row["institution_type"] = (
                            project.projectbillingdetails.institution.institution_type.name
                            if hasattr(project, "projectbillingdetails")
                            and project.projectbillingdetails.institution
                            and project.projectbillingdetails.institution.institution_type
                            else ""
                        )
                        data_row["institution_name"] = (
                            project.projectbillingdetails.institution.name
                            if hasattr(project, "projectbillingdetails") and project.projectbillingdetails.institution
                            else ""
                        )
                    data_row["combination_active"] = project.active
                else:
                    account: Account = Account.objects.get(pk=user_combination[1])
                    data_row["account"] = account.name
                    data_row["account_type"] = account.type.name if account.type else ""
                    data_row["combination_active"] = account.active
            data.add_row(data_row)
        data.rows.sort(key=lambda x: x["first"])

    summary = SummaryDisplayTable()
    summary.add_header(("item", "Item"))
    summary.add_row({"item": f"Unique {'combinations' if combination else 'users'}"})
    if CoreFacility and CoreFacility.objects.exists():
        summary.add_row({"item": "By core facility"})
        for core_facility in CoreFacility.objects.all():
            summary.add_row({"item": f"{core_facility.name}"})
        summary.add_row({"item": "N/A"})
    if ProjectDiscipline.objects.exists():
        summary.add_row({"item": "By project discipline"})
        for discipline in ProjectDiscipline.objects.all():
            summary.add_row({"item": f"{discipline.name}"})
        summary.add_row({"item": "N/A"})
    if AccountType.objects.exists():
        summary.add_row({"item": "By account type"})
        for account_type in AccountType.objects.all():
            summary.add_row({"item": f"{account_type.name}"})
        summary.add_row({"item": "N/A"})
    if RateCategory and RateCategory.objects.exists():
        summary.add_row({"item": "By project rate category"})
        for category in RateCategory.objects.all():
            summary.add_row({"item": f"{category.name}"})
    if InstitutionType and InstitutionType.objects.exists():
        summary.add_row({"item": "By institution type"})
        for institution_type in InstitutionType.objects.all():
            summary.add_row({"item": f"{institution_type.name}"})
        summary.add_row({"item": "N/A"})
    summary.add_row({"item": "By remote status"})
    summary.add_row({"item": "Remote"})
    summary.add_row({"item": "On-site"})

    if split_by_month:
        for month in get_monthly_rule(start, end):
            month_key = f"month_{month.strftime('%Y')}_{month.strftime('%m')}"
            summary.add_header((month_key, month.strftime("%b %Y")))
            month_start, month_end = get_month_range(month)
            add_summary_info(params, summary, monthly_start or month_start, month_end, combination, month_key)
    else:
        summary.add_header(("value", "Value"))
        add_summary_info(params, summary, start, end, combination)

    report_key = (
        "unique_user_project"
        if combination == "project_id"
        else "unique_user_account"
        if combination
        else "unique_users"
    )
    if params.get_bool("export"):
        return report_export([summary, data], report_key, start, end)
    dictionary = {
        "data": data,
        "summary": summary,
    }
    return render(
        request, "NEMO_reports/report_active_users.html", reporting_dictionary(report_key, params, dictionary)
    )


def add_summary_info(
    parameters: ReportingParameters, summary: SummaryDisplayTable, start, end, combination, summary_key=None
):
    RateCategory = get_rate_category()
    CoreFacility = get_core_facility()
    InstitutionType = get_institution_type()

    summary_key = summary_key or "value"
    summary.rows[0][summary_key] = len(get_unique_user_combinations(parameters, start, end, combination=combination))
    current_row = 1
    if CoreFacility and CoreFacility.objects.exists():
        for facility in CoreFacility.objects.all():
            current_row += 1
            f_filter = Q(core_facility_id=facility.id)
            summary.rows[current_row][summary_key] = len(
                get_unique_user_combinations(parameters, start, end, combination, f_filter)
            )
        # Add general (None) subtotal too
        current_row += 1
        f_filter = Q(core_facility_id__isnull=True)
        summary.rows[current_row][summary_key] = len(
            get_unique_user_combinations(parameters, start, end, combination, f_filter)
        )
        current_row += 1  # For mid table header
    if ProjectDiscipline.objects.exists():
        for discipline in ProjectDiscipline.objects.all():
            current_row += 1
            p_filter = Q(project__discipline=discipline)
            summary.rows[current_row][summary_key] = len(
                get_unique_user_combinations(parameters, start, end, combination, p_filter)
            )
        current_row += 1
        p_filter = Q(project__discipline__isnull=True)
        summary.rows[current_row][summary_key] = len(
            get_unique_user_combinations(parameters, start, end, combination, p_filter)
        )
        current_row += 1  # For mid table header
    if AccountType.objects.exists():
        for account_type in AccountType.objects.all():
            current_row += 1
            a_filter = Q(project__account__type=account_type)
            summary.rows[current_row][summary_key] = len(
                get_unique_user_combinations(parameters, start, end, combination, a_filter)
            )
        current_row += 1
        a_filter = Q(project__account__type__isnull=True)
        summary.rows[current_row][summary_key] = len(
            get_unique_user_combinations(parameters, start, end, combination, a_filter)
        )
        current_row += 1  # For mid table header
    if RateCategory and RateCategory.objects.exists():
        for category in RateCategory.objects.all():
            current_row += 1
            r_filter = Q(project__projectbillingdetails__category=category)
            summary.rows[current_row][summary_key] = len(
                get_unique_user_combinations(parameters, start, end, combination, r_filter)
            )
        current_row += 1  # For mid table header
    if InstitutionType and InstitutionType.objects.exists():
        for institution_type in InstitutionType.objects.all():
            current_row += 1
            institution_type_filter = Q(project__projectbillingdetails__institution__institution_type=institution_type)
            summary.rows[current_row][summary_key] = len(
                get_unique_user_combinations(parameters, start, end, combination, institution_type_filter)
            )
        current_row += 1
        institution_type_filter = Q(project__projectbillingdetails__institution__institution_type__isnull=True)
        summary.rows[current_row][summary_key] = len(
            get_unique_user_combinations(parameters, start, end, combination, institution_type_filter)
        )
        current_row += 1
    current_row += 1
    summary.rows[current_row][summary_key] = len(
        get_unique_user_combinations(parameters, start, end, combination, Q(remote=True))
    )
    current_row += 1
    summary.rows[current_row][summary_key] = len(
        get_unique_user_combinations(parameters, start, end, combination, Q(remote=False))
    )


def get_unique_user_combinations(
    params: ReportingParameters,
    start,
    end,
    combination: str,
    extra_filter: Q = None,
) -> Set[Tuple[int, int]]:
    user_combinations = set("")
    combination = [combination] if combination else []
    if params.get_bool("tool_usage", "on"):
        tool_usage = (
            usage_events(start, end).only(*["user_id", "end"] + combination).values_list(*["user_id"] + combination)
        )
        if extra_filter:
            tool_usage = tool_usage.filter(extra_filter)
        user_combinations.update(set(tool_usage))
    if params.get_bool("area_access", "on"):
        area_records = (
            area_access(start, end)
            .only(*["customer_id", "end"] + combination)
            .values_list(*["customer_id"] + combination)
        )
        if extra_filter:
            area_records = area_records.filter(extra_filter)
        user_combinations.update(set(area_records))
    if params.get_bool("staff_charges", "on"):
        staff_work = (
            staff_charges(start, end)
            .only(*["customer_id", "end"] + combination)
            .values_list(*["customer_id"] + combination)
        )
        if extra_filter:
            staff_work = staff_work.filter(extra_filter)
        user_combinations.update(set(staff_work))
    if params.get_bool("consumables", "on"):
        consumables = (
            consumable_withdraws(start, end)
            .only(*["customer_id", "date"] + combination)
            .values_list(*["customer_id"] + combination)
        )
        if extra_filter:
            consumables = consumables.filter(extra_filter)
        user_combinations.update(set(consumables))
    if params.get_bool("training", "on"):
        trainings = (
            training_sessions(start, end)
            .only(*["trainee_id", "date"] + combination)
            .values_list(*["trainee_id"] + combination)
        )
        if extra_filter:
            trainings = trainings.filter(extra_filter)
        user_combinations.update(set(trainings))
    if params.get_bool("missed_reservations", "on"):
        missed = (
            missed_reservations(start, end)
            .only(*["user_id", "end"] + combination)
            .values_list(*["user_id"] + combination)
        )
        if extra_filter:
            missed = missed.filter(extra_filter)
        user_combinations.update(set(missed))
    if billing_installed() and params.get_bool("custom_charges", "on"):
        custom = (
            custom_charges(start, end)
            .only(*["customer_id", "date"] + combination)
            .values_list(*["customer_id"] + combination)
        )
        if extra_filter:
            custom = custom.filter(extra_filter)
        user_combinations.update(set(custom))
    return user_combinations
