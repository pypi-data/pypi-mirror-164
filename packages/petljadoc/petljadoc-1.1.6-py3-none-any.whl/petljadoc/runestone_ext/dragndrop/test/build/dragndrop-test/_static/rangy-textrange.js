/**
 * Text range module for Rangy.
 * Text-based manipulation and searching of ranges and selections.
 *
 * Features
 *
 * - Ability to move range boundaries by character or word offsets
 * - Customizable word tokenizer
 * - Ignore text nodes inside <script> or <style> elements or those hidden by CSS display and visibility properties
 * - Do not ignore text nodes that are outside normal document flow
 * - Range findText method to search for text or regex within the page or within a range. Flags for whole words and case
 *   sensitivity
 * - Selection and range save/restore as text offsets within a node
 * - Methods to return visible text within a range or selection
 * - innerText method for elements
 *
 * References
 *
 * https://www.w3.org/Bugs/Public/show_bug.cgi?id=13145
 * http://aryeh.name/spec/innertext/innertext.html
 * http://dvcs.w3.org/hg/editing/raw-file/tip/editing.html
 *
 * Part of Rangy, a cross-browser JavaScript range and selection library
 * http://code.google.com/p/rangy/
 *
 * Depends on Rangy core.
 *
 * Copyright 2012, Tim Down
 * Licensed under the MIT license.
 * Version: 1.3alpha.681
 * Build date: 20 July 2012
 */
rangy.createModule("TextRange",function(a,b){function v(a){return a&&(a.nodeType==1&&!/^(inline(-block|-table)?|none)$/.test(J(a))||a.nodeType==9||a.nodeType==11)}function w(a){var b=a.lastChild;return b?w(b):a}function x(a){return f.isCharacterDataNode(a)||!/^(area|base|basefont|br|col|frame|hr|img|input|isindex|link|meta|param)$/i.test(a.nodeName)}function y(a){var b=[];while(a.parentNode)b.unshift(a.parentNode),a=a.parentNode;return b}function z(a){return y(a).concat([a])}function A(a){while(a&&!a.nextSibling)a=a.parentNode;return a?a.nextSibling:null}function B(a,b){return!b&&a.hasChildNodes()?a.firstChild:A(a)}function C(a){var b=a.previousSibling;if(b){a=b;while(a.hasChildNodes())a=a.lastChild;return a}var c=a.parentNode;return c&&c.nodeType==1?c:null}function D(a){var b=z(a);for(var c=0,d=b.length;c<d;++c)if(b[c].nodeType==1&&J(b[c])=="none")return!0;return!1}function E(a){var b;return a.nodeType==3&&(b=a.parentNode)&&u(b,"visibility")=="hidden"}function F(a){if(!a||a.nodeType!=3)return!1;var b=a.data;if(b=="")return!0;var c=a.parentNode;if(!c||c.nodeType!=1)return!1;var d=u(a.parentNode,"whiteSpace");return/^[\t\n\r ]+$/.test(b)&&/^(normal|nowrap)$/.test(d)||/^[\t\r ]+$/.test(b)&&d=="pre-line"}function G(a){if(a.data=="")return!0;if(!F(a))return!1;var b=a.parentNode;return b?D(a)?!0:!1:!0}function J(a,b){var c=u(a,"display",b),d=a.tagName.toLowerCase();return c=="block"&&H&&I.hasOwnProperty(d)?I[d]:c}function K(a){var b=a.nodeType;return b==7||b==8||D(a)||/^(script|style)$/i.test(a.nodeName)||E(a)||G(a)}function L(a,b){var c=a.nodeType;return c==7||c==8||c==1&&J(a,b)=="none"}function M(a){if(!K(a)){if(a.nodeType==3)return!0;for(var b=a.firstChild;b;b=b.nextSibling)if(M(b))return!0}return!1}function N(a){return new h(a.startContainer,a.startOffset)}function O(a){return new h(a.endContainer,a.endOffset)}function P(a,b,c,d,e,f){this.character=a,this.position=b,this.isLeadingSpace=c,this.isTrailingSpace=d,this.isBr=e,this.collapsible=f}function Q(a){if(a.tagName.toLowerCase()=="br")return"";switch(J(a)){case"inline":var b=a.lastChild;while(b){if(!L(b))return b.nodeType==1?Q(b):"";b=b.previousSibling}break;case"inline-block":case"inline-table":case"none":case"table-column":case"table-column-group":break;case"table-cell":return"  ";default:return M(a)?"\n":""}return""}function R(a){switch(J(a)){case"inline":case"inline-block":case"inline-table":case"none":case"table-column":case"table-column-group":case"table-cell":break;default:return M(a)?"\n":""}return""}function S(a){var b=a.node,c=a.offset;if(!b)return null;var d,e,g;return c==f.getNodeLength(b)?(d=b.parentNode,e=d?f.getNodeIndex(b)+1:0):f.isCharacterDataNode(b)?(d=b,e=c+1):(g=b.childNodes[c],x(g)?(d=g,e=0):(d=b,e=c+1)),d?new h(d,e):null}function T(a){if(!a)return null;var b=a.node,c=a.offset,d,e,g;return c==0?(d=b.parentNode,e=d?f.getNodeIndex(b):0):f.isCharacterDataNode(b)?(d=b,e=c-1):(g=b.childNodes[c-1],x(g)?(d=g,e=f.getNodeLength(g)):(d=b,e=c-1)),d?new h(d,e):null}function U(a){var b=S(a);if(!b)return null;var c=b.node,d=b;return K(c)&&(d=new h(c.parentNode,f.getNodeIndex(c)+1)),d}function V(a){var b=T(a);if(!b)return null;var c=b.node,d=b;return K(c)&&(d=new h(c.parentNode,f.getNodeIndex(c))),d}function W(a,b){return{characterOptions:b}}function X(a){var b=null,c=!1,d=u(a.parentNode,"whiteSpace"),e=d=="pre-line";if(e)b=k,c=!0;else if(d=="normal"||d=="nowrap")b=j,c=!0;return{node:a,text:a.data,spaceRegex:b,collapseSpaces:c,preLine:e}}function Y(a,b){var c=a.node,d=a.offset,e="",f=!1,g=!1,h=!1,i=!1;if(d>0)if(c.nodeType==3){var j=c.data,k=j.charAt(d-1),l=b.nodeInfo;if(!l||l.node!==c)b.nodeInfo=l=X(c);var m=l.spaceRegex;l.collapseSpaces?m.test(k)?(i=!0,!(d>1&&m.test(j.charAt(d-2)))&&(!l.preLine||j.charAt(d)!=="\n"||!r)&&(e=" ")):e=k:e=k}else{var n=c.childNodes[d-1];n&&n.nodeType==1&&!K(n)&&(n.tagName.toLowerCase()=="br"?(e="\n",h=!0):(e=Q(n),e&&(g=i=!0)));if(!e){var o=c.childNodes[d];o&&o.nodeType==1&&!K(o)&&(e=R(o),e&&(f=!0))}}return new P(e,a,f,g,h,i)}function Z(a,b){var c=a,d;while(c=U(c)){d=Y(c,b);if(d.character!=="")return d}return null}function $(a,b,c){var d=Y(a,b),e=d.character,f,g;if(!e)return d;if(j.test(e)){if(!c){var h=a,i,k;c=[];while(h=V(h)){i=Y(h,b),k=i.character;if(k!==""){c.unshift(i);if(k!=" "&&k!="\n")break}}}return g=c[c.length-1],!g,e===" "&&d.collapsible&&(!g||g.isTrailingSpace||g.character=="\n")?d.character="":d.collapsible&&(!(f=Z(a,b))||f.character=="\n"&&f.collapsesPrecedingSpace())?d.character="":e==="\n"&&!d.collapsible&&(!(f=Z(a,b))||f.isTrailingSpace)&&(d.character=""),d}return d}function ab(a,c,d,e){function m(){var a=null;return l||(c||(k=U(k)),k?(a=$(k,j),d&&k.equals(d)&&(l=!0)):l=!0,c&&(k=V(k))),a}var g=i({},_),h=e?i(g,e):g,j=W(f.getWindow(a.node),h);d&&(c?K(d.node)&&(d=V(d)):K(d.node)&&(d=U(d)));var k=a,l=!1,n,o=!1;return{next:function(){if(o)return o=!1,n;var a;while(a=m())if(a.character)return n=a,a},rewind:function(){if(!n)throw b.createError("createCharacterIterator: cannot rewind. Only one position can be rewound.");o=!0},dispose:function(){a=d=j=null}}}function bb(a,b){function f(b,c,d){var f=a.slice(b,c),g={isWord:d,chars:f,toString:function(){return f.join("")}};for(var h=0,i=f.length;h<i;++h)f[h].token=g;e.push(g)}var c=a.join(""),d,e=[],g=0,h,i;while(d=b.wordRegex.exec(c)){h=d.index,i=h+d[0].length,h>g&&f(g,h,!1);if(b.includeTrailingSpace)while(m.test(a[i]))++i;f(h,i,!0),g=i}return g<a.length&&f(g,a.length,!1),e}function db(a,b){function f(a){var b,e,f=[],g=a?c:d,h=!1,i=!1;while(b=g.next()){e=b.character;if(l.test(e))i&&(i=!1,h=!0);else{if(h){g.rewind();break}i=!0}f.push(b)}return f}function m(a){var b=[];for(var c=0;c<a.length;++c)b[c]="(word: "+a[c]+", is word: "+a[c].isWord+")";return b}var c=ab(a,!1),d=ab(a,!0),e=b.tokenizer,g=f(!0),h=f(!1).reverse(),i=e(h.concat(g),b),j=g.length?i.slice(cb(i,g[0].token)):[],k=h.length?i.slice(0,cb(i,h.pop().token)+1):[];return{nextEndToken:function(){var a;return j.length==1&&!(a=j[0]).isWord&&(j=e(a.chars.concat(f(!0)),b)),j.shift()},previousStartToken:function(){var a;return k.length==1&&!(a=k[0]).isWord&&(k=e(f(!1).reverse().concat(a.chars),b)),k.pop()},dispose:function(){c.dispose(),d.dispose(),j=k=null}}}function fb(a){var b,c;return a?(b=a.language||o,c={},i(c,eb[b]||eb[o]),i(c,a),c):eb[o]}function hb(a,b,c,f){var g=0,h=a,i,j,k,l,m=Math.abs(c),n;if(c!==0){var o=c<0;switch(b){case d:j=ab(a,o);while((i=j.next())&&g<m)++g,l=i;k=i,j.dispose();break;case e:var p=db(a,f),q=o?p.previousStartToken:p.nextEndToken;while((n=q())&&g<m)n.isWord&&(++g,l=o?n.chars[0]:n.chars[n.chars.length-1]);break;default:throw new Error("movePositionBy: unit '"+b+"' not implemented")}l&&(h=l.position),o?(h=V(h),g=-g):l&&l.isLeadingSpace&&(b==e&&(j=ab(a,!1),k=j.next(),j.dispose()),k&&(h=V(k.position)))}return{position:h,unitsMoved:g}}function ib(a){return ab(N(a),!1,O(a))}function jb(a){var b=[],c=ib(a),d;while(d=c.next())b.push(d);return c.dispose(),b}function kb(b,c,d){var e=a.createRange(b.node);e.setStart(b.node,b.offset),e.setEnd(c.node,c.offset);var f=!e.expand("word",d);return e.detach(),f}function lb(a,b,c,d,e){function r(a,b){var c=V(i[a].position),d=i[b-1].position,f=!e.wholeWordsOnly||kb(c,d,e.wordOptions);return{startPos:c,endPos:d,valid:f}}var f=p(e.direction),g=ab(a,f,f?N(d):O(d)),h="",i=[],j,k,l,m,n,o,q=null;while(j=g.next()){k=j.character,k=j.character,!c&&!e.caseSensitive&&(k=k.toLowerCase()),f?(i.unshift(j),h=k+h):(i.push(j),h+=k);if(c){n=b.exec(h);if(n)if(o){l=n.index,m=l+n[0].length;if(!f&&m<h.length||f&&l>0){q=r(l,m);break}}else o=!0}else if((l=h.indexOf(b))!=-1){q=r(l,l+b.length);break}}return o&&(q=r(l,m)),g.dispose(),q}function mb(a,b){return function(c,f,g){typeof f=="undefined"&&(f=c,c=d),c==e&&(g=fb(g));var h=a;b&&(h=f>=0,this.collapse(!h));var i=h?N:O,j=hb(i(this),c,f,g),k=j.position;return this[h?"setStart":"setEnd"](k.node,k.offset),j.unitsMoved}}a.requireModules(["WrappedSelection"]);var c="undefined",d="character",e="word",f=a.dom,g=a.util,h=f.DomPosition,i=g.extend,j=/^[ \t\f\r\n]+$/,k=/^[ \t\f\r]+$/,l=/^[\t-\r \u0085\u00A0\u1680\u180E\u2000-\u200B\u2028\u2029\u202F\u205F\u3000]+$/,m=/^[\t \u00A0\u1680\u180E\u2000-\u200B\u202F\u205F\u3000]+$/,n=/^[\n-\r\u0085\u2028\u2029]$/,o="en",p=a.Selection.isDirectionBackward,q=!1,r=!1,s=!0,t=document.createElement("div");g.isHostProperty(t,"innerText")&&(t.innerHTML="<p>&nbsp; </p><p></p>",document.body.appendChild(t),q=!/ /.test(t.innerText),document.body.removeChild(t));var u;typeof window.getComputedStyle!=c?u=function(a,b,c){return(c||f.getWindow(a)).getComputedStyle(a,null)[b]}:typeof document.documentElement.currentStyle!=c?u=function(a,b){return a.currentStyle[b]}:b.fail("No means of obtaining computed style properties found");var H;(function(){var a=document.createElement("table");document.body.appendChild(a),H=u(a,"display")=="block",document.body.removeChild(a)})(),a.features.tableCssDisplayBlock=H;var I={table:"table",caption:"table-caption",colgroup:"table-column-group",col:"table-column",thead:"table-header-group",tbody:"table-row-group",tfoot:"table-footer-group",tr:"table-row",td:"table-cell",th:"table-cell"};P.prototype.toString=function(){return this.character},P.prototype.collapsesPrecedingSpace=function(){return this.character=="\n"&&(this.isBr&&r||this.isTrailingSpace&&q)};var _={ignoreSpaceBeforeLineBreak:!0},cb=Array.prototype.indexOf?function(a,b){return a.indexOf(b)}:function(a,b){for(var c=0,d=a.length;c<d;++c)if(a[c]===b)return c;return-1},eb={en:{wordRegex:/[a-z0-9]+('[a-z0-9]+)*/gi,includeTrailingSpace:!1,tokenizer:bb}},gb={caseSensitive:!1,withinRange:null,wholeWordsOnly:!1,wrap:!1,direction:"forward",wordOptions:null};i(f,{nextNode:B,previousNode:C,hasInnerText:M}),i(a.rangePrototype,{moveStart:mb(!0,!1),moveEnd:mb(!1,!1),move:mb(!0,!0),expand:function(a,b){var c=!1;a||(a=d);if(a==e){b=fb(b);var f=N(this),g=O(this),h=db(f,b),i=h.nextEndToken(),j=V(i.chars[0].position),k,l;if(this.collapsed)k=i;else{var m=db(g,b);k=m.previousStartToken()}return l=k.chars[k.chars.length-1].position,j.equals(f)||(this.setStart(j.node,j.offset),c=!0),l.equals(g)||(this.setEnd(l.node,l.offset),c=!0),c}return this.moveEnd(d,1)},text:function(){return this.collapsed?"":jb(this).join("")},selectCharacters:function(a,b,c){this.selectNodeContents(a),this.collapse(!0),this.moveStart(b),this.collapse(!0),this.moveEnd(c-b)},toCharacterRange:function(a){a||(a=document.body);var b=a.parentNode,c=f.getNodeIndex(a),d=f.comparePoints(this.startContainer,this.endContainer,b,c)==-1,e=this.cloneRange(),g,h;return d?(e.setStart(this.startContainer,this.startOffset),e.setEnd(b,c),g=-e.text().length):(e.setStart(b,c),e.setEnd(this.startContainer,this.startOffset),g=e.text().length),h=g+this.text().length,{start:g,end:h}},findText:function(b,c){var d=i({},gb),e=c?i(d,c):d;e.wholeWordsOnly&&(e.wordOptions=fb(e.wordOptions),e.wordOptions.includeTrailingSpace=!1);var f=p(e.direction),g=e.withinRange;g||(g=a.createRange(),g.selectNodeContents(this.getDocument()));var h=b,j=!1;typeof h=="string"?e.caseSensitive||(h=h.toLowerCase()):j=!0;var k=f?O(this):N(this),l=g.comparePoint(k.node,k.offset);l===-1?k=N(g):l===1&&(k=O(g));var m=k,n=!1,o;for(;;){o=lb(m,h,j,g,e);if(o){if(o.valid)return this.setStart(o.startPos.node,o.startPos.offset),this.setEnd(o.endPos.node,o.endPos.offset),!0;m=f?o.startPos:o.endPos}else{if(!e.wrap||!!n)return!1;g=g.cloneRange(),f?(m=O(g),g.setStart(k.node,k.offset)):(m=N(g),g.setEnd(k.node,k.offset)),n=!0}}},pasteHtml:function(a){this.deleteContents();if(a){var b=this.createContextualFragment(a),c=b.lastChild;this.insertNode(b),this.collapseAfter(c)}}}),i(a.selectionPrototype,{expand:function(a,b){var c=this.getAllRanges(),d=c.length,e=this.isBackward();for(var f=0,g=c.length;f<g;++f)c[f].expand(a,b);this.removeAllRanges(),e&&d==1?this.addRange(c[0],!0):this.setRanges(c)},move:function(a,b,c){if(this.focusNode){this.collapse(this.focusNode,this.focusOffset);var d=this.getRangeAt(0);d.move(a,b,c),this.setSingleRange(d)}},selectCharacters:function(b,c,d,e){var f=a.createRange(b);f.selectCharacters(b,c,d),this.setSingleRange(f,e)},saveCharacterRanges:function(a){var b=this.getAllRanges(),c=b.length,d=[],e=c==1&&this.isBackward();for(var f=0,g=b.length;f<g;++f)d[f]={range:b[f].toCharacterRange(a),backward:e};return d},restoreCharacterRanges:function(b,c){this.removeAllRanges();for(var d=0,e=c.length,f,g;d<e;++d)g=c[d],f=a.createRange(b),f.selectCharacters(b,g.range.start,g.range.end),this.addRange(f,g.backward)},text:function(){var a=[];for(var b=0,c=this.rangeCount;b<c;++b)a[b]=this.getRangeAt(b).text();return a.join("")}}),a.innerText=function(b){var c=a.createRange(b);c.selectNodeContents(b);var d=c.text();return c.detach(),d},a.createWordIterator=function(a,b,c,d){d=fb(d);var e=new h(a,b),f=db(e,d),g=p(c);return{next:function(){return g?f.previousStartToken():f.nextEndToken()},dispose:function(){f.dispose(),this.next=function(){}}}},a.textRange={isBlockNode:v,isCollapsedWhitespaceNode:G,nextPosition:S,previousPosition:T,nextVisiblePosition:U,previousVisiblePosition:V}})