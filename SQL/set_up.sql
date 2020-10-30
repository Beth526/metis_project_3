

\connect clinical_trials;

DROP TABLE basic_info;
CREATE TABLE basic_info(
  Idx INT,
  Rank INT,
  NCTId TEXT,
  BriefTitle TEXT,
  Condition TEXT,
  Keyword TEXT,
  OverallStatus TEXT,
  WhyStopped TEXT,
  StartDate TEXT,
  PrimaryCompletionDate TEXT,
  CompletionDate TEXT,
  ReferencePMID TEXT,
  ReferenceType TEXT,
  IsFDARegulatedDrug TEXT,
  IsFDARegulatedDevice TEXT,
  IsUnapprovedDevice TEXT,
  HasExpandedAccess TEXT,
  IsUSExport TEXT,
  OversightHasDMC TEXT
);

DROP TABLE outcomes;
CREATE TABLE outcomes(
  Idx INT,
  Rank INT,
  NCTId TEXT,
  PrimaryOutcomeMeasure TEXT,
  PrimaryOutcomeDescription TEXT,
  PrimaryOutcomeTimeFrame TEXT,
  SecondaryOutcomeMeasure TEXT,
  SecondaryOutcomeDescription TEXT,
  SecondaryOutcomeTimeFrame TEXT,
  OtherOutcomeMeasure TEXT,
  OtherOutcomeDescription TEXT,
  OtherOutcomeTimeFrame TEXT
);

DROP TABLE study_design;
CREATE TABLE study_design(
  Idx INT,
  Rank INT,
  NCTId TEXT,
  DesignPrimaryPurpose TEXT,
  Phase TEXT,
  DesignInterventionModel TEXT,
  DesignInterventionModelDescription TEXT,
  DesignWhoMasked TEXT,
  DesignAllocation TEXT,
  EnrollmentCount TEXT,
  EnrollmentType TEXT,
  ArmGroupLabel TEXT,
  ArmGroupType TEXT,
  ArmGroupDescription TEXT,
  InterventionType TEXT,
  InterventionName TEXT,
  InterventionOtherName TEXT,
  InterventionDescription TEXT
);

DROP TABLE eligibility;
CREATE TABLE eligibility(
  Idx INT,
  Rank INT,
  NCTId TEXT,
  Gender TEXT,
  GenderBased TEXT,
  MinimumAge TEXT,
  MaximumAge TEXT,
  HealthyVolunteers TEXT,
  EligibilityCriteria TEXT,
  IPDSharing TEXT
);

DROP TABLE investigators;
CREATE TABLE investigators(
  Idx INT,
  Rank INT,
  NCTId TEXT,
  ResponsiblePartyType TEXT,
  ResponsiblePartyInvestigatorAffiliation TEXT,
  LeadSponsorName TEXT,
  CollaboratorName TEXT,
  OverallOfficialAffiliation TEXT,
  LocationFacility TEXT,
  LocationCity TEXT,
  LocationState TEXT,
  LocationCountry TEXT
  );

\copy basic_info FROM 'All_BasicInfo_combined.csv' DELIMITER '`';
\copy outcomes FROM 'All_Outcomes_combined.csv' DELIMITER '`';
\copy study_design FROM 'All_StudyDesign_combined.csv' DELIMITER '`';
\copy eligibility FROM 'All_eligibility_combined.csv' DELIMITER '`';
\copy investigators FROM 'All_investigators_combined.csv' DELIMITER '`';
