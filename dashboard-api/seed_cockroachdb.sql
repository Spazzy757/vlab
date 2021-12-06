
DROP TABLE IF EXISTS optimization_reports;
DROP TABLE IF EXISTS studies;


CREATE TABLE studies(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    name string NOT NULL,
    slug string NOT NULL,
    CONSTRAINT unique_name UNIQUE(name),
    CONSTRAINT unique_slug UNIQUE(slug)
);

INSERT INTO studies 
  (name, slug, created, id) 
VALUES 
  ('Iron overload in men', 'iron-overload-in-men', '2021-01-03', '36634740-0a26-44a3-b69d-d1338af5126c'),
  ('Consuming carbs less often leads to better fat adaptation', 'consuming-carbs-less-often-leads-to-better-fat-adaptation', '2021-01-02', 'f6112068-5227-4e17-b255-2b80df8745e9'),
  ('Most used programming language for api development', 'most-used-programming-language-for-api-development', '2021-01-04', 'a5601576-08d9-486b-adc9-9b981b7f103b');


CREATE TABLE optimization_reports(
  study_id UUID NOT NULL REFERENCES studies(id),
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
  report_type VARCHAR NOT NULL,
  details JSON NOT NULL,
  CONSTRAINT unique_report UNIQUE(study_id, created)
);

INSERT INTO optimization_reports
  (study_id, created, report_type, details)
VALUES
  ('36634740-0a26-44a3-b69d-d1338af5126c', '2021-01-03', 'FACEBOOK_OPTIMIZATION','{ 
    "25-spain-male": {
      "current_budget": 720000,
      "desired_percentage": 5,
      "current_percentage": 0,
      "expected_percentage": 0,
      "desired_participants": null,
      "current_participants": 0,
      "expected_participants": 0,
      "current_price_per_participants": 0
    },
    "25-spain-female": {
      "current_budget": 720000,
      "desired_percentage": 5,
      "current_percentage": 0,
      "expected_percentage": 0,
      "desired_participants": 2400,
      "current_participants": 0,
      "expected_participants": 0,
      "current_price_per_participants": 0
    }
  }'),
  ('36634740-0a26-44a3-b69d-d1338af5126c', '2021-01-04', 'FACEBOOK_OPTIMIZATION','{ 
    "25-spain-male": {
      "current_budget": 720000,
      "desired_percentage": 5,
      "current_percentage": 8.25,
      "expected_percentage": 8.67,
      "desired_participants": null,
      "current_participants": 59,
      "expected_participants": 64,
      "current_price_per_participants": 100
    },
    "25-spain-female": {
      "current_budget": 720000,
      "desired_percentage": 5,
      "current_percentage": 3.5,
      "expected_percentage": 2.98,
      "desired_participants": 2400,
      "current_participants": 25,
      "expected_participants": 22,
      "current_price_per_participants": 300
    }
  }');