<?xml version="1.0" encoding="UTF-8"?>
<sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>Indice UCS</sld:Name>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>Indice UCS</sld:Name>
      <sld:Title>Indice UCS</sld:Title>
      <sld:Abstract>abstract</sld:Abstract>
      <sld:FeatureTypeStyle>
        <sld:Name>name</sld:Name>
        <sld:FeatureTypeName>Feature</sld:FeatureTypeName>
        <sld:SemanticTypeIdentifier>generic:geometry</sld:SemanticTypeIdentifier>
        <sld:SemanticTypeIdentifier>colorbrewer:quantile:personal</sld:SemanticTypeIdentifier>
		<sld:Rule>
		<sld:Name>0 - 20</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>0</ogc:Literal>
              </ogc:PropertyIsGreaterThanOrEqualTo>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>20</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#eaf2fb</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
		<sld:Name>20 -30</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>20</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>30</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#dceaf6</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
		<sld:Name>30 -40</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>30</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>40</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#d0e1f2</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
		<sld:Name>40 -50</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>40</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>50</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#c1d9ed</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
		<sld:Name>50 -60</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>50</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>60</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#abd0e6</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
		<sld:Name>60 -70</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>60</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>70</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#94c4df</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
		<sld:Name>70 -80</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>70</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>80</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#79b5d9</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
		<sld:Name>80 -100</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>80</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>100</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#60a7d2</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
		<sld:Name>100 -120</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>100</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>120</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#4a98c9</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
		<sld:Name>120 -140</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>120</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>140</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#3787c0</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
		<sld:Name>140 -160</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>140</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>160</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#2575b7</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
		<sld:Name>160 -180</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>160</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>180</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#1764ab</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
		<sld:Name>180 -200</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>180</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>200</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#0a539e</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
		<sld:Rule>
		<sld:Name>200 -230</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThan>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>200</ogc:Literal>
              </ogc:PropertyIsGreaterThan>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>ucs</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>230</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#084285</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>25</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>