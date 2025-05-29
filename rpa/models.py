from django.db import models
from django.contrib.auth.models import User

# Create your models here.

Q1A = [
    ('A', 'Have not estimated the repetitions'),
    ('B', 'Very little repetitive tasks required'),
    ('C', 'Some repetitive tasks required'),
    ('D', 'Many repetitive tasks required'),
    ('E', 'Extensive repetitive tasks required'),

]

Q2A = [
    ('A', 'Not sure of the status or health of the process'),
    ('B', 'Some of the process is currently executed in business'),
    ('C', 'New process is required altogether'),
    ('D', 'Enhancement to existing process is required'),
    ('E', 'Entire process is currently executed in business'),

]

Q3A = [
    ('A', 'No human intervention in process'),
    ('B', 'Single person performing task'),
    ('C', 'Few people performing same task'),
    ('D', 'Many people performing same task'),

]

Q4A = [
    ('A', 'Not sure how often the process would need to run'),
    ('B', 'Once off process (ad hoc remediation)'),
    ('C', 'Once daily'),
    ('D', 'Once weekly'),
    ('E', 'Once monthly'),
    ('F', 'Once quarterly'),
    ('G', 'Once annually'),
    ('H', 'Multiple times daily'),
    ('I', 'Multiple times weekly'),
    ('J', 'Multiple times monthly'),
    ('K', 'Multiple times quarterly'),

]

Q5A = [
    ('A', 'Up to 10'),
    ('B', 'Up to 50'),
    ('C', 'Up to 100'),
    ('D', 'Up to 1,000'),
    ('E', 'Up to 10,000'),
    ('F', 'Up to 100,000'),
    ('G', 'Up to 1,000,000'),
    ('H', 'More than 1,000,000'),

]

Q6A = [
    ('A', 'Not sure how much time is required per cycle'),
    ('B', 'Less than 30 mins per cycle'),
    ('C', '30-60mins per cycle'),
    ('D', '60-90mins per cycle'),
    ('E', '90-120mins per cycle'),
    ('F', '120-180mins per cycle'),
    ('G', '180-360mins per cycle'),
    ('H', '360-520mins per cycle'),
('I', '520-900min per cycle'),
    ('J', 'More than 900mins per cycle'),

]

Q7A = [
    ('A', 'No human decisions required'),
    ('B', 'Simple rule or parameter based decisions'),
    ('C', 'Complex rule or parameter based decisions'),
    ('D', 'Decisions require judgement calls not based on parameters'),
    ('E', 'Not sure, need to investigate'),

]

Q8A = [
    ('A', 'Not sure if there are exceptions'),
    ('B', 'No exceptions'),
    ('C', 'Alternate workflow managed via systems'),
    ('D', 'Alternate workflow managed by humans'),
    ('E', 'Process generates error and fails'),
('F', 'Process terminates '),

]

Q9A = [
    ('A', 'Not sure if data is required'),
    ('B', 'Manual input data'),
    ('C', 'Unstructured data (eg email / word documents)'),
    ('D', 'Structured data sources (data file / spread sheet)'),
    ('E', 'Combination of sources'),

]

Q10A = [
    ('A', 'All sources are maintained by IM'),
    ('B', 'Some of the sources are maintained by IM'),
    ('C', 'None of the sources are maintained by IM'),
    ('D', 'Not sure, need to investigate'),

]

Q11A = [
    ('A', 'Yes, other verifiable sources'),
    ('B', 'Yes, combination of sources and feed types'),
    ('C', 'Yes, external data from website'),
    ('D', 'Yes, external information via data feed or file'),
    ('E', 'Yes, external data from web subscription service'),
('F', 'No external data used / required'),

]

Q12A = [
    ('A', 'No own investigation has taken place on contract / legal compliance'),
    ('B', 'Risk group has identified compliance issues to be resolved'),
    ('C', 'Risk group have not been engaged to review requirements'),
    ('D', 'Risk group in process of investigating compliance requirements'),
    ('E', 'Risk group has validated legal compliance requirements'),
('F', 'Risk group have signed off on all compliance requirements'),
('G', 'No exposure to 3rd party information risk'),

]

Q13A = [
    ('A', 'Input data not yet identified'),
    ('B', 'Some input data is identified '),
    ('C', 'Most input data is identified'),
    ('D', 'All input data is identified'),
    ('E', 'Most input data is identified and available'),
('F', 'All input data is identified and available'),

]

Q14A = [
    ('A', 'Not sure what options are available'),
    ('B', 'No other options considered'),
    ('C', 'Investigated options but too expensive'),
    ('D', 'Investigated options but not suited'),
    ('E', 'Investigated but no other options identified'),
('F', 'Options available but not viable'),
('G', 'Options available but would not meet requirement'),
    ('H', 'Options are not desirable due to impact on business or customer'),

]

Q15A = [
    ('A', 'None at present'),
    ('B', 'Yes, but not in the next 2 years'),
    ('C', 'Yes, but not in the next 1 year'),
    ('D', 'Yes, but not in the next 6 months'),
    ('E', 'Yes, but not in the next 3 months'),
('F', 'Yes, within next 30 days'),
('G', 'Yes, busy with change right now'),
    ('H', 'Not sure, need to investigate'),

]

Q16A = [
    ('A', 'Not sure if threats are identified or known'),
    ('B', 'No known threats are this time'),
    ('C', 'Threat suspected but not confirmed'),
    ('D', 'Customer impact threat identified'),
    ('E', 'Key mand dependency identified'),
('F', 'Regulatory compliance threat identified'),
('G', 'Information security / risk threat identified'),

]

Q17A = [
    ('A', 'Not able to support initiative'),
    ('B', 'Not sure what is required to support initiative'),
    ('C', 'Yes, but only limited time available'),
    ('D', 'Yes, but require additional resources'),
    ('E', 'Yes, but require additional skills'),
('F', 'Yes, key resources will be allocated to the initiative'),

]

Q18A = [
    ('A', 'Not sure what environments we have in place'),
    ('B', 'No, need to be secured'),
    ('C', 'Yes, but not adequate'),
    ('D', 'Yes, have DEV, QA and Prod environments'),
    ('E', 'Yes, have DEV, QA, Pre-Prod and Prod environments'),

]

Q19A = [
    ('A', 'Not sure whether data is representative or available'),
    ('B', 'Data not available at present'),
    ('C', 'Although data not available. It can be obtained'),
    ('D', 'Although data available, it is not entirely suited or aligned'),
    ('E', 'Accurate data available for some systems but not representative'),
('F', 'Accurate data available for all systems but not representative'),
('G', 'Accurate and representative data available for some systems'),
    ('H', 'Accurate and representative data available for all systems'),

]

Q20A = [
    ('A', 'Executive override obtained - proceed without risk sign-off'),
    ('B', 'Risk assessment done, supported and signed off'),
    ('C', 'Risk assessment done and supported, but not signed off'),
    ('D', 'Risk assessment raised concerns, not signed off'),
    ('E', 'No risk assessment performed yet'),
('F', 'Not sure if risk assessment is required'),

]

Q21A = [
    ('A', 'Yes, within the same process'),
    ('B', 'Yes, within different process but similar in functionality'),
    ('C', 'Yes, but totally different application'),
    ('D', 'No BOTs active for the area'),
    ('E', 'Not sure, need to investigate'),

]


Recurrence = [
    ('Non-recurring', 'Non-recurring'),
    ('Recurring specific date', 'Recurring specific date'),
    ('Recurring daily', 'Recurring daily'),
    ('Recurring weekly', 'Recurring weekly'),
    ('Recurring monthly', 'Recurring monthly'),
('Recurring quarterly', 'Recurring quarterly'),
    ('Recurring annually', 'Recurring annually'),
    ('Recurring event', 'Recurring event'),

]

TRIGGER  = [
    ('Month-end', 'Month-end'),
    ('Quarter-end', 'Quarter-end'),
    ('Year-end', 'Year-end'),
    ('Last day of month', 'Last day of month'),
    ('First day of year', 'First day of year'),
('Last day of year', 'Last day of year'),
    ('Specific date only', 'Specific date only'),
    ('Specific day only', 'Specific day only'),
('Specific week-day', 'Specific week-day'),
    ('Event driven', 'Event driven'),
    ('Ad hoc', 'Ad hoc'),

]

DAY = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),


]

EVENT_TYPE = [
    ('Activity', 'Activity'),
    ('Alert', 'Alert'),
    ('Exception', 'Exception'),
    ('Excess', 'Excess'),
    ('Procedure', 'Procedure'),
('Schedule', 'Schedule'),
    ('Update', 'Update'),


]

CRITICALITY = [
    ('Mission critical', 'Mission critical'),
    ('Mandatory', 'Mandatory'),
    ('Very important', 'Very important'),
    ('Important', 'Important'),
    ('Less important', 'Less important'),
('Not important', 'Not important'),

]

IMPACT = [
    ('Extreme', 'Extreme'),
    ('Severe', 'Severe'),
    ('Moderate', 'Moderate'),
    ('Low', 'Low'),
    ('Negligible', 'Negligible'),

]

LATE_TOLERANCE = [
    ('Zero tolerance', 'Zero tolerance'),
    ('Max 30min', 'Max 30min'),
    ('Max 1 hour', 'Max 1 hour'),
    ('Max 4 hours', 'Max 4 hours'),
    ('Max 1 day', 'Max 1 day'),
('Max 1 week', 'Max 1 week'),
    ('Max 1 month', 'Max 1 month'),
('More than 1 month', 'More than 1 month'),
]

TIME_DEPENDENCIES = [
    ('No dependencies', 'No dependencies'),
    ('Wait for event / trigger', 'Wait for event / trigger'),
    ('After a certain time', 'After a certain time'),
    ('Before a certain time', 'Before a certain time'),
    ('Between specific times', 'Between specific times'),
('Anytime during business day', 'Anytime during business day'),
    ('Outside normal business hours', 'Outside normal business hours'),
('Overnight only', 'Overnight only'),
]

WAIT = [
    ('Do not wait', 'Do not wait'),
    ('No specific time', 'No specific time'),
    ('00:00:00', '00:00:00'),
    ('01:00:00', '01:00:00'),
    ('02:00:00', '02:00:00'),
('03:00:00', '03:00:00'),
    ('04:00:00', '04:00:00'),
('05:00:00', '05:00:00'),
    ('06:00:00', '06:00:00'),
('07:00:00', '07:00:00'),
    ('08:00:00', '08:00:00'),
    ('09:00:00', '09:00:00'),
('10:00:00', '10:00:00'),
    ('11:00:00', '11:00:00'),
('12:00:00', '12:00:00'),
    ('13:00:00', '13:00:00'),
('14:00:00', '14:00:00'),
    ('15:00:00', '15:00:00'),
    ('16:00:00', '16:00:00'),
('17:00:00', '17:00:00'),
    ('18:00:00', '18:00:00'),
('19:00:00', '19:00:00'),
    ('21:00:00', '21:00:00'),
('22:00:00', '22:00:00'),
('23:00:00', '23:00:00'),
]

COMPLEXITY = [
    ('No idea', 'No idea'),
    ('Simple linear process', 'Simple linear process'),
    ('Some process dependencies', 'Some process dependencies'),
    ('Many process interdependencies', 'Many process interdependencies'),
    ('Medium non-linear process', 'Medium non-linear process'),
('Complex process with iterations', 'Complex process with iterations'),
]

UNDERSTANDING = [
    ('No idea', 'No idea'),
    ('Mostly', 'Mostly'),
    ('Somewhat', 'Somewhat'),
    ('Not really', 'Not really'),
    ('Not at all', 'Not at all'),
]

OPTIMISED = [
    ('Yes - Recently', 'Yes - Recently'),
    ('Yes - Some time ago', 'Yes - Some time ago'),
    ('Busy re-engineering process now', 'Busy re-engineering process now'),
    ('No - considering it', 'No - considering it'),
    ('No - not necessary', 'No - not necessary'),
    ('No - not planned', 'No - not planned'),
]

STABLE = [
    ('Stable for 6 months', 'Stable for 6 months'),
    ('Small changes within 6 months', 'Small changes within 6 months'),
    ('Many changes over past 6 months', 'Many changes over past 6 months'),
    ('Planned changes in next 90 days', 'Planned changes in next 90 days'),
    ('New process - less than 3 months', 'New process - less than 3 months'),
    ('Not sure - need to find out', 'Not sure - need to find out'),
]

DOCUMENTATION = [
    ('Yes - detailed and current', 'Yes - detailed and current'),
    ('Yes - detailed but not current', 'Yes - detailed but not current'),
    ('Yes - not detailed', 'Yes - not detailed'),
    ('Yes - some gaps', 'Yes - some gaps'),
    ('Yes - very old', 'Yes - very old'),
    ('No', 'No'),
    ('Not sure - need to find out', 'Not sure - need to find out'),
]

CUSTOMER_FACING = [
    ('No - affects department', 'No - affects department'),
    ('No - affects business unit', 'No - affects business unit'),
    ('Internal stakeholders', 'Internal stakeholders'),
    ('Group internal stakeholders', 'Group internal stakeholders'),
    ('External stakeholders', 'External stakeholders'),
    ('Customer impacts', 'Customer impacts'),
]

REGULATED = [
    ('No', 'No'),
    ('Yes - low impact', 'Yes - low impact'),
    ('Yes - Medium impact', 'Yes - Medium impact'),
    ('Yes - High impact', 'Yes - High impact'),
    ('Yes - Ultra high impact', 'Yes - Ultra high impact'),
    ('Yes - license threat', 'Yes - license threat'),
]

SELF_CONTAINED = [
    ('Yes - stand-alone', 'Yes - stand-alone'),
    ('Yes -  limited interaction', 'Yes -  limited interaction'),
    ('No - some dependencies', 'No - some dependencies'),
    ('No - many dependencies', 'No - many dependencies'),
    ('No - extensive and involved', 'No - extensive and involved'),
]

ERRORS = [
    ('No - none in past 3 months', 'No - none in past 3 months'),
    ('No - some in past 3 months', 'No - some in past 3 months'),
    ('Yes - human errors', 'Yes - human errors'),
    ('Yes - data incorrect', 'Yes - data incorrect'),
    ('Yes - exceptions noted', 'Yes - exceptions noted'),
('Yes - unexpected results', 'Yes - unexpected results'),
    ('Yes - process fails', 'Yes - process fails'),
]

MANUAL_INTERVENTION = [
    ('No', 'No'),
    ('Yes', 'Yes'),
    ('Not Sure', 'Not Sure'),
]

class BusinessUnit(models.Model):
    name = models.CharField(max_length=64, null=True,)
    head = models.CharField(max_length=64, null=True, )

    #utility Fields
    created_date = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)


class Process(models.Model):
    name = models.CharField(max_length=64, null=True,)
    head = models.CharField(max_length=64, null=True, )
    business_unit = models.ForeignKey(BusinessUnit, models.CASCADE, blank=True, null=True)

    recurrence = models.CharField(max_length=64, null=True, choices=Recurrence)
    trigger = models.CharField(max_length=64, null=True, choices=TRIGGER)
    day = models.CharField(max_length=64, null=True, choices=TRIGGER)
    date  = models.DateTimeField(null=True, blank=True)
    event_type = models.CharField(max_length=64, null=True, choices=EVENT_TYPE)
    criticality = models.CharField(max_length=64, null=True, choices=CRITICALITY)
    impact_if_failed = models.CharField(max_length=64, null=True, choices=IMPACT)
    impact_if_late = models.CharField(max_length=64, null=True, choices=IMPACT)
    impact_of_time_overun = models.CharField(max_length=64, null=True, choices=IMPACT)
    late_tolerance = models.CharField(max_length=64, null=True, choices=LATE_TOLERANCE)
    time_dependencies = models.CharField(max_length=64, null=True, choices=TIME_DEPENDENCIES)
    wait_until_time = models.CharField(max_length=64, null=True, choices=WAIT)
    complete_by_time = models.CharField(max_length=64, null=True, choices=WAIT)
    complexity = models.CharField(max_length=64, null=True, choices=CRITICALITY)
    understanding = models.CharField(max_length=64, null=True, choices=UNDERSTANDING)
    optimised = models.CharField(max_length=64, null=True, choices=OPTIMISED)
    stable = models.CharField(max_length=64, null=True, choices=STABLE)
    documentation = models.CharField(max_length=64, null=True, choices=DOCUMENTATION)
    customer_facing = models.CharField(max_length=64, null=True, choices=CUSTOMER_FACING)
    regulated = models.CharField(max_length=64, null=True, choices=REGULATED)
    self_contained = models.CharField(max_length=64, null=True, choices=SELF_CONTAINED)
    errors = models.CharField(max_length=64, null=True, choices=ERRORS)
    manual_intervention = models.CharField(max_length=64, null=True, choices=MANUAL_INTERVENTION)

    #utility Fields
    created_date = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)




class Answers(models.Model):
    process = models.ForeignKey(Process, models.CASCADE, blank=True, null=True)
    Qone = models.CharField(max_length=64, null=True, choices=Q1A)
    Qtwo = models.CharField(max_length=64, null=True, choices=Q2A)
    Qthree = models.CharField(max_length=64, null=True, choices=Q3A)
    Qfour = models.CharField(max_length=64, null=True, choices=Q4A)
    Qfive = models.CharField(max_length=64, null=True, choices=Q5A)
    Qsix = models.CharField(max_length=64, null=True, choices=Q6A)
    Qseven = models.CharField(max_length=64, null=True, choices=Q7A)
    Qeight = models.CharField(max_length=64, null=True, choices=Q8A)
    Qnine = models.CharField(max_length=64, null=True, choices=Q9A)
    Qten = models.CharField(max_length=64, null=True, choices=Q10A)
    Qeleven = models.CharField(max_length=64, null=True, choices=Q11A)
    Qtwelve = models.CharField(max_length=64, null=True, choices=Q12A)
    Qthirteen = models.CharField(max_length=64, null=True, choices=Q13A)
    Qfourteen = models.CharField(max_length=64, null=True, choices=Q14A)
    Qfifteen = models.CharField(max_length=64, null=True, choices=Q15A)
    Qsixteen = models.CharField(max_length=64, null=True, choices=Q16A)
    Qseventeen = models.CharField(max_length=64, null=True, choices=Q17A)
    Qeighteen = models.CharField(max_length=64, null=True, choices=Q18A)
    Qnineteen = models.CharField(max_length=64, null=True, choices=Q19A)
    Qtwenty = models.CharField(max_length=64, null=True, choices=Q20A)
    Qtwentyone = models.CharField(max_length=64, null=True, choices=Q21A)

    #utility Fields
    created_date = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)


class BusinessUnitManagers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    assigned = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=64, null=True,)
    business_unit = models.ForeignKey(BusinessUnit, models.CASCADE, blank=True, null=True)



