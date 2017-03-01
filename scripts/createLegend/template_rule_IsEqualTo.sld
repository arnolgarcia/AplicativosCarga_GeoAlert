		<sld:Rule>
          <sld:Name>rulename</sld:Name>
          <ogc:Filter>
            <ogc:PropertyIsEqualTo>
              <ogc:PropertyName>param_atributo</ogc:PropertyName>
              <ogc:Literal>param_valorclase</ogc:Literal>
            </ogc:PropertyIsEqualTo>
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
				<ogc:Literal>pixelsize</ogc:Literal>
              </sld:Size>
            </sld:Graphic>
          </sld:PointSymbolizer>
        </sld:Rule>