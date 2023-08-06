/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { LabIcon } from '@jupyterlab/ui-components';

import pyIconSvg from '../style/icons/py-logo.svg';
import rIconSvg from '../style/icons/r-logo.svg';

export const rIcon = new LabIcon({
  name: 'meganote:rIcon',
  svgstr: rIconSvg
});
export const pyIcon = new LabIcon({
  name: 'meganote:pyIcon',
  svgstr: pyIconSvg
});

/**
 * A utilities class for handling LabIcons.
 */
export class IconUtil {
  static encode(icon: LabIcon): string {
    return 'data:image/svg+xml;utf8,' + encodeURIComponent(icon.svgstr);
  }

  private static colorizedIcons: { [key: string]: LabIcon } = {};

  static colorize(
    icon: LabIcon,
    fillColor?: string,
    strokeColor?: string
  ): LabIcon {
    const iconName = `${icon.name}${fillColor ? ':' + fillColor : ''}${
      strokeColor ? ':' + strokeColor : ''
    }`;

    if (this.colorizedIcons[iconName]) {
      return this.colorizedIcons[iconName];
    }

    let svgstr = icon.svgstr;

    if (fillColor) {
      svgstr = svgstr.replace(/fill="[^(none)]+?"/gi, `fill="${fillColor}"`);
    }
    if (strokeColor) {
      svgstr = svgstr.replace(
        /stroke="[^(none)]+?"/gi,
        `stroke="${strokeColor}"`
      );
    }

    const coloredIcon = LabIcon.resolve({
      icon: {
        name: iconName,
        svgstr: svgstr
      }
    });

    this.colorizedIcons[iconName] = coloredIcon;

    return coloredIcon;
  }
}
