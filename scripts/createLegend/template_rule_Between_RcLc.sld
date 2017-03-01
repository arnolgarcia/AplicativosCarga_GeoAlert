		<sld:Rule>
		<sld:Name>param_rulename</sld:Name>
          <ogc:Filter>
            <ogc:And>
              <ogc:PropertyIsGreaterThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>param_atributo</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>param_rangomin</ogc:Literal>
              </ogc:PropertyIsGreaterThanOrEqualTo>
              <ogc:PropertyIsLessThanOrEqualTo>
                <ogc:Function name="property">
					<ogc:Literal>param_atributo</ogc:Literal>
				</ogc:Function>
                <ogc:Literal>param_rangomax</ogc:Literal>
              </ogc:PropertyIsLessThanOrEqualTo>
            </ogc:And>
          </ogc:Filter>
          <sld:PointSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
            <sld:Graphic>
              <sld:Mark>
                <sld:WellKnownName>square</sld:WellKnownName>
                <sld:Fill>
                  <sld:CssParameter name="fill">param_colorhex</sld:CssParameter>
                </sld:Fill>
                <Stroke>
                  <CssParameter name="stroke-opacity">0</CssParameter>
                </Stroke>
              </sld:Mark>
              <sld:Size>
				<ogc:Literal>param_pixelsize</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>