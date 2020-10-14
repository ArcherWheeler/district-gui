import clip_districts
import color_districts

states = {
    'alabama': 'AL',
    'alaska': 'AK',
    'arizona': 'AZ',
    'arkansas': 'AR',
    'california': 'CA',
    'delaware': 'DE',
    'florida': 'FL',
    'georgia': 'GA',
    'hawaii': 'AL',
    'idaho': 'ID',
    'illinois': 'IL',
    'indiana': 'ID',
    'iowa': 'IA',
    'kansas': 'KS',
    'kentucky': 'KY',
    'louisiana': 'LA',
    'maine': 'ME',
    'maryland': 'MD',
    'massachusetts': 'MA',
    'michigan': 'MI',
    'minnesota': 'MN',
    'mississippi': 'MS',
    'missouri': 'MO',
    'montana': 'MT',
    'nebraska': 'NE',
    'nevada': 'NV',
    'new_hampshire': 'NH',
    'new_jersey': 'NJ',
    'new_mexico': 'NM',
    'new_york': 'NY',
    'north_carolina': 'NC',
    'north_dakota': 'ND',
    'ohio': 'OH',
    'oklahoma': 'OK',
    'oregon': 'OR',
    'pennsylvania': 'PA',
    'rhode_island': 'RI',
    'south_carolina': 'SC',
    'south_dakota': 'SD',
    'tennessee': 'TN',
    'texas': 'TX',
    'utah': 'UT',
    'vermont': 'VT',
    'virginia': 'VA',
    'washington': 'WA',
    'west_virginia': 'WV',
    'wisconsin': 'WI',
    'wyoming': 'WY'
}

# for state in states:
#     clip_districts.clip_district(state, states[state])
#     color_districts.color_district(state)

clip_districts.clip_district('alabama', 'AL')
color_districts.color_district('alabama')