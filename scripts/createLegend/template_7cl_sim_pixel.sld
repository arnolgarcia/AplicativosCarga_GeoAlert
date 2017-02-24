<?xml version="1.0" encoding="UTF-8"?>
<sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
  <sld:NamedLayer>
    <sld:Name>titulo</sld:Name>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>titulo</sld:Name>
      <sld:Title>titulo</sld:Title>
      <sld:Abstract>abstract</sld:Abstract>
      <sld:FeatureTypeStyle>
        <sld:Name>name</sld:Name>
        <sld:FeatureTypeName>Feature</sld:FeatureTypeName>
        <sld:SemanticTypeIdentifier>generic:geometry</sld:SemanticTypeIdentifier>
        <sld:SemanticTypeIdentifier>colorbrewer:quantile:personal</sld:SemanticTypeIdentifier>

		<sld:Rule>
          <sld:Name>rulename1</sld:Name>
          <ogc:Filter>
            <ogc:PropertyIsLessThan>
              <ogc:Function name="property">
                <ogc:Literal>atributo</ogc:Literal>
              </ogc:Function>
              <ogc:Mul>
                <ogc:Literal>saturacion</ogc:Literal>
                <ogc:Literal>-1</ogc:Literal>
              </ogc:Mul>
            </ogc:PropertyIsLessThan>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#D53E4F</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>pixelsize</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

		<sld:Rule>
		<sld:Name>rulename2</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>atributo</ogc:Literal>
				</ogc:Function>
                <ogc:Mul>
					<ogc:Literal>saturacion</ogc:Literal>
					<ogc:Literal>-1</ogc:Literal>
                </ogc:Mul>
              </ogc:PropertyIsGreaterThanOrEqualTo>
              <ogc:PropertyIsLessThan>
                <ogc:Function name="property">
					<ogc:Literal>atributo</ogc:Literal>
				</ogc:Function>
                <ogc:Mul>
				  <ogc:Literal>saturacion</ogc:Literal>
                  <ogc:Literal>-0.6</ogc:Literal>
                </ogc:Mul>
              </ogc:PropertyIsLessThan>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#FC8D59</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>pixelsize</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

		<sld:Rule>
          <sld:Name>rulename3</sld:Name>
		  <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>atributo</ogc:Literal>
				</ogc:Function>
                <ogc:Mul>
				  <ogc:Literal>saturacion</ogc:Literal>
                  <ogc:Literal>-0.6</ogc:Literal>
                </ogc:Mul>
              </ogc:PropertyIsGreaterThanOrEqualTo>
              <ogc:PropertyIsLessThan>
                <ogc:Function name="property">
					<ogc:Literal>atributo</ogc:Literal>
				</ogc:Function>
                <ogc:Mul>
				  <ogc:Literal>saturacion</ogc:Literal>
                  <ogc:Literal>-0.2</ogc:Literal>
                </ogc:Mul>
              </ogc:PropertyIsLessThan>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#FEE08B</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>pixelsize</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

		<sld:Rule>
          <sld:Name>rulename4</sld:Name>
		  <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>atributo</ogc:Literal>
				</ogc:Function>
                <ogc:Mul>
				  <ogc:Literal>saturacion</ogc:Literal>
                  <ogc:Literal>-0.2</ogc:Literal>
                </ogc:Mul>
              </ogc:PropertyIsGreaterThanOrEqualTo>
              <ogc:PropertyIsLessThan>
                <ogc:Function name="property">
					<ogc:Literal>atributo</ogc:Literal>
				</ogc:Function>
                <ogc:Mul>
				  <ogc:Literal>saturacion</ogc:Literal>
                  <ogc:Literal>0.2</ogc:Literal>
                </ogc:Mul>
              </ogc:PropertyIsLessThan>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#00FF00</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>pixelsize</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

		<sld:Rule>
          <sld:Name>rulename5</sld:Name>
		  <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>atributo</ogc:Literal>
				</ogc:Function>
                <ogc:Mul>
				  <ogc:Literal>saturacion</ogc:Literal>
                  <ogc:Literal>0.2</ogc:Literal>
                </ogc:Mul>
              </ogc:PropertyIsGreaterThanOrEqualTo>
              <ogc:PropertyIsLessThan>
                <ogc:Function name="property">
					<ogc:Literal>atributo</ogc:Literal>
                </ogc:Function>
                <ogc:Mul>
				  <ogc:Literal>saturacion</ogc:Literal>
                  <ogc:Literal>0.6</ogc:Literal>
                </ogc:Mul>
              </ogc:PropertyIsLessThan>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#8EBF80</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>pixelsize</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

		<sld:Rule>
          <sld:Name>rulename6</sld:Name>
		  <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>atributo</ogc:Literal>
				</ogc:Function>
                <ogc:Mul>
				  <ogc:Literal>saturacion</ogc:Literal>
                  <ogc:Literal>0.6</ogc:Literal>
                </ogc:Mul>
              </ogc:PropertyIsGreaterThanOrEqualTo>
              <ogc:PropertyIsLessThan>
                <ogc:Function name="property">
					<ogc:Literal>atributo</ogc:Literal>
				</ogc:Function>
                <ogc:Mul>
				  <ogc:Literal>saturacion</ogc:Literal>
                  <ogc:Literal>1</ogc:Literal>
                </ogc:Mul>
              </ogc:PropertyIsLessThan>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#9CCBED</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>pixelsize</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

		<sld:Rule>
          <sld:Name>rulename7</sld:Name><ogc:Filter>
            <ogc:PropertyIsGreaterThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>atributo</ogc:Literal>
				</ogc:Function>
              <ogc:Mul>
				<ogc:Literal>saturacion</ogc:Literal>
                <ogc:Literal>1</ogc:Literal>
              </ogc:Mul>
            </ogc:PropertyIsGreaterThanOrEqualTo>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">#3288BD</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>pixelsize</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>

      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </sld:NamedLayer>
</sld:StyledLayerDescriptor>
