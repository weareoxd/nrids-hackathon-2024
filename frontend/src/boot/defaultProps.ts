import { QBtn } from 'quasar';
import { boot } from 'quasar/wrappers';

export default boot(({}) => {
  // default "no-caps" prop to prevent all uppercase button text
  QBtn.props.noCaps = { type: Boolean, default: true };
});
