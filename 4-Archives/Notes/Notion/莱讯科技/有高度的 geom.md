# 有高度的 geom

```sql
ALTER TABLE madinat_xmc.t_polygon 
  ALTER COLUMN geom TYPE geometry(PolygonZ)
    USING ST_Force3D(geom);
```

```sql
SELECT ST_AsText(geom) FROM madinat_xmc.t_polygon
WHERE id='3116f6ff-cd8f-4449-ba48-ae74e7262041';
```

```sql
SELECT ST_GeometryType(geom) FROM madinat_xmc.t_polygon
WHERE id='3116f6ff-cd8f-4449-ba48-ae74e7262041';
```

```sql
SELECT ST_GeomFromGeoJSON(ST_AsGeoJSON(geom)) FROM madinat_xmc.t_polygon
WHERE id='3116f6ff-cd8f-4449-ba48-ae74e7262041';
```

```sql
UPDATE madinat_xmc.t_polygon 
SET geom=ST_SetSRID(ST_GeomFromGeoJSON(ST_AsGeoJSON(geom)),4326) 
WHERE id='3116f6ff-cd8f-4449-ba48-ae74e7262041';

UPDATE madinat_xmc.t_polygon 
SET geom=ST_SetSRID(ST_GeomFromGeoJSON(
	'{
	  "type": "Polygon",
	  "coordinates": [
			[
			  [
					110.024751978796,
					39.7374827647249,
					0
			  ],
			  [
					110.025622788835,
					39.7374900789708,
					3
			  ],
			  [
					110.025623343284,
					39.7374540578743,
					3
			  ],
			  [
					110.024741267836,
					39.7374465522464,
					3
			  ],
			  [
					110.024643491217,
					39.7374458277466,
					3
			  ],
			  [
					110.024642983319,
					39.7374818492328,
					3
			  ],
			  [
					110.024751978796,
					39.7374827647249,
					0
			  ]
			]
	  ]
	}'
),4326) 
WHERE id='3116f6ff-cd8f-4449-ba48-ae74e7262041';
```

```json
{
  "type": "Polygon",
  "coordinates": [
    [
      [
        110.024751978796,
        39.7374827647249
      ],
      [
        110.025622788835,
        39.7374900789708
      ],
      [
        110.025623343284,
        39.7374540578743
      ],
      [
        110.024741267836,
        39.7374465522464
      ],
      [
        110.024643491217,
        39.7374458277466
      ],
      [
        110.024642983319,
        39.7374818492328
      ],
      [
        110.024751978796,
        39.7374827647249
      ]
    ]
  ]
}
```